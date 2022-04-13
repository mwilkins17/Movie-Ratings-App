"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """User model for movie ratings app."""
    
    __tablename__ = "users"
    #table name is users
    
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        """Show info about user class"""
        
        return f"<User ID={self.user_id}, Email={self.email}, Password={self.password}>"
    
    
    
class Movie(db.Model):
    """Movie model for movie ratings app."""
    
    __tablename__ = 'movies'
    #table name is movies
    
    movie_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False, unique=True)
    overview = db.Column(db.Text, nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)
    poster_path = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        """show info about movie class"""

        return f"""<Movie ID={self.movie_id},
                Title={self.title},
                Overview={self.overview},
                Release Date={self.release_date},
                Poster Path={self.poster_path}>"""
    

class Rating(db.Model):
    """Rating model for movie ratings app."""
    
    rating_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    score = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.movie.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user.id"))
    
    def __repr__(self):
        
        return f"""<Rating Rating Id={self.rating_id},
                Score={self.score},
                Movie ID={self.movie_id}, 
                User ID={self.user_id}"""



def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
