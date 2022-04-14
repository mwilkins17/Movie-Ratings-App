"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """View Homepage"""

    return render_template('homepage.html')

@app.route('/movies')
def movies():
    
    movies = crud.get_movies()

    return render_template('all_movies.html', movies=movies)

@app.route("/movies/<movie_id>")
def show_movie(movie_id):

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)

@app.route("/users")
def users():

    users = crud.get_users()

    return render_template('all_users.html', users=users)


@app.route("/users", methods =["POST"])
def register_user():
       
    email = request.form.get("email")
    password = request.form.get("password")
    user = crud.get_user_by_email(email)
    
    if user:
        flash("User already registered")
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("User created successfully; you may now log in")
    
    return redirect("/")        


@app.route("/users/<user_id>")
def show_user(user_id):

    user = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user=user)

@app.route("/login", methods=["POST"])
def user_log_in():
    """Log a user in"""    
    
    email = request.form.get("email")
    password = request.form.get("password")
    user = crud.get_user_by_email(email)
    
    if not user or user.password != password:
        flash("Invalid email or password. Try again.")
        return redirect("/")
    else:
        #log in by storing users email in session
        session['user_email'] = user.email
        flash("Successfully logged in!")

    return redirect("/movies")

@app.route("/movies/<movie_id>/ratings", methods=["POST"])
def create_ratings(movie_id):
    """Create a New Rating for a Movie"""

    # make sure that a user is logged in before they can give a rating!
    logged_in_email = session.get("user_email")
    rating_score = request.form.get("user-rating")

    # make sure user inputs their email and rating
    if logged_in_email is None:
        flash("Sorry! You need to log in before rating a movie!")
    elif rating_score is None:
        flash("Sorry! You need to select a score for your rating!")
    else:
        user = crud.get_user_by_email(logged_in_email)
        movie = crud.get_movie_by_id(movie_id)

        rating = crud.create_rating(user, movie, int(rating_score))
        db.session.add(rating)
        db.session.commit()

        flash(f"Congrats! You rated this movie {rating_score} out of 5!")
    
    return redirect(f"/movies/{movie_id}")


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
