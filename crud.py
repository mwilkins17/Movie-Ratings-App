"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db


# Functions start here!


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""
    
    movie = Movie(
            title=title,
            overview=overview, 
            release_date=release_date,
            poster_path=poster_path,
            )
    
    return movie

def create_rating(user, movie, score):
    #user=string, movie=string, score=int
    """Create and return a new rating"""
    
    rating = Rating(
        user=user,
        movie=movie,
        score=score,
    )
    
    return rating

def get_movies():
    """Show All Movies"""

    return Movie.query.all()

def get_movie_by_id(movie_id):
    """Return movie by movie id"""
    
    return Movie.query.get(movie_id)

def get_users():
    """Show All Users"""
    
    return User.query.all()

def get_user_by_id(user_id):
    """Return User by User ID"""
    
    return User.query.get(user_id)

def get_user_by_email(email):
    """Return a User by Email"""
    
    # if User.query.filter(User.email == email).first():
    #     return User.query.filter(User.email == email).first()
    # else:
    #     return None
    return User.query.filter(User.email == email).first()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)