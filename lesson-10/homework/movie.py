import requests
import random

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.themoviedb.org/3"

def get_genres():
    """Fetch all available movie genres from TMDb API."""
    url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    
    if response.status_code == 200:
        genres = response.json()["genres"]
        return {genre["name"].lower(): genre["id"] for genre in genres}
    else:
        print("Error fetching genres!")
        return {}

def get_movies_by_genre(genre_id):
    """Fetch movies for a given genre ID."""
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()["results"]
    else:
        print("Error fetching movies!")
        return []

def recommend_movie(genre):
    """Recommend a random movie from the chosen genre."""
    genres = get_genres()
    
    if genre.lower() in genres:
        genre_id = genres[genre.lower()]
        movies = get_movies_by_genre(genre_id)
        
        if movies:
            movie = random.choice(movies)
            print("\n🎬 Movie Recommendation:")
            print(f"Title: {movie['title']}")
            print(f"Overview: {movie['overview']}")
            print(f"Rating: {movie['vote_average']}/10")
        else:
            print("No movies found for this genre.")
    else:
        print("Invalid genre! Please try again.")


user_genre = input("Enter a movie genre (e.g., Action, Comedy, Drama): ")
recommend_movie(user_genre)