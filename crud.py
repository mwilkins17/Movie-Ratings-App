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
    
    return Movie.query.get(movie_id)


if __name__ == '__main__':
    from server import app
    connect_to_db(app)