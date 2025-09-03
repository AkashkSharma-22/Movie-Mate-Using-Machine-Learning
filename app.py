import streamlit as st
import pickle
import pandas as pd
import requests
import os
import gdown
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)

# Get environment variables with default values
API_KEY = os.getenv('API_KEY', '479916d10972f80eeeee140a1ad3b701')
MOVIE_DICT_ID = os.getenv('MOVIE_DICT_ID', '1LiCe2ZG552tjBztNSHRBtBKSkOdQUaEQ')
SIMILARITY_ID = os.getenv('SIMILARITY_ID', '1O8daZuVfRh8vUukVWdyS23NPghrj2kbd')


def download_if_missing(file_id, output_name):
    if not os.path.exists(output_name):
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, output_name, quiet=False)

# Download files only if they're not already present
download_if_missing(SIMILARITY_ID, "similarity.pkl")
download_if_missing(MOVIE_DICT_ID, "movie_dict.pkl")

# Function to fetch movie details from TMDb API
def fetch_movie_details(movie_title):
    """
    Fetch movie details including poster URL and rating from TMDb API
    """
    try:
        # Clean movie title for better search results
        clean_title = movie_title.split('(')[0].strip()  # Remove year in parentheses
        
        # Search for the movie with improved parameters
        search_url = f"https://api.themoviedb.org/3/search/movie"
        search_params = {
            'api_key': API_KEY,
            'query': clean_title,
            'language': 'en-US',
            'include_adult': False,
            'page': 1
        }
        
        search_response = requests.get(search_url, params=search_params, timeout=5)
        search_response.raise_for_status()
        search_data = search_response.json()
        
        if search_data['results'] and len(search_data['results']) > 0:
            # Find the best match
            movie = search_data['results'][0]
            poster_path = movie.get('poster_path')
            rating = movie.get('vote_average', 'N/A')
            
            if poster_path:
                # Use high-quality poster (w780 instead of w500)
                poster_url = f"https://image.tmdb.org/t/p/w780{poster_path}"
            else:
                # Fallback to movie title-based placeholder
                title_safe = clean_title.replace(' ', '+')
                poster_url = f"https://via.placeholder.com/500x750/1a1a1a/ffffff?text={title_safe}"
                
            return poster_url, str(rating) if rating != 'N/A' else '7.0'
        else:
            # Fallback for movies not found in API
            title_safe = clean_title.replace(' ', '+')
            poster_url = f"https://via.placeholder.com/500x750/2c2c2c/ffffff?text={title_safe}"
            return poster_url, '7.0'
            
    except requests.exceptions.RequestException as e:
        print(f"Network error for {movie_title}: {str(e)}")
        # Fallback for network issues
        title_safe = movie_title.replace(' ', '+')
        poster_url = f"https://via.placeholder.com/500x750/cccccc/333333?text={title_safe}"
        return poster_url, '7.0'
    except Exception as e:
        print(f"Error fetching details for {movie_title}: {str(e)}")
        # Generic fallback
        title_safe = movie_title.replace(' ', '+')
        poster_url = f"https://via.placeholder.com/500x750/cccccc/333333?text={title_safe}"
        return poster_url, '7.0'


# Recommendation function with API integration
def recommend(movie_title):
    try:
        movie_index = movies_list[movies_list['title'] == movie_title].index[0]
        distances = similarity[movie_index]
        movies_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        
        recommended_movies = []
        recommended_posters = []
        recommended_ratings = []
        
        for i in movies_indices:
            title = movies_list.iloc[i[0]].title
            poster, rating = fetch_movie_details(title)
            
            recommended_movies.append(title)
            recommended_posters.append(poster)
            recommended_ratings.append(rating)

        return recommended_movies, recommended_posters, recommended_ratings
    except IndexError:
        # Handle case when movie title is not found
        st.error(f"Movie '{movie_title}' not found in database. Please select from available movies.")
        return [], [], []


# ----------------- Streamlit UI -----------------
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 Movie Recommender System")

# Load movies and similarity data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies_list = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Dropdown to select movie
selected_movie_name = st.selectbox(
    "Select a movie to get recommendations:",
    movies_list['title'].values
)

# Show recommendations
if st.button("Recommend"):
    names, posters, ratings = recommend(selected_movie_name)

    st.subheader("Top 5 Recommendations for You:")

    # Layout: show 5 recommendations in a row
    cols = st.columns(5)
    for idx, (col, name, poster, rating) in enumerate(zip(cols, names, posters, ratings)):
        with col:
            if poster:  # show poster if available
                st.image(poster, width=200)
            st.markdown(f"<p style='text-align:center'><b>#{idx+1}: {name}</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align:center'>⭐ {rating}/10</p>", unsafe_allow_html=True)
