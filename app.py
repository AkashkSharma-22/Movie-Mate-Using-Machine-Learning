import streamlit as st
import pickle
import pandas as pd
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def fetch_poster(movie_id):
    api_key = os.getenv('API_KEY')
    if not api_key:
        st.error("TMDb API key not found. Please set API_KEY environment variable.")
        return None
    
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            poster_path = data.get('poster_path')
            if poster_path:
                return "https://image.tmdb.org/t/p/w500/" + poster_path
        return None
    except:
        return None

def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        
        recommended_movies = []
        recommended_movies_posters = []
        
        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movies.append(movies.iloc[i[0]].title)
            poster = fetch_poster(movie_id)
            recommended_movies_posters.append(poster)
        
        return recommended_movies, recommended_movies_posters
    except Exception as e:
        st.error(f"Error generating recommendations: {str(e)}")
        return [], []

# Load data with error handling
@st.cache_data
def load_data():
    try:
        movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
        similarity = pickle.load(open('similarity.pkl', 'rb'))
        return pd.DataFrame(movies_dict), similarity
    except FileNotFoundError:
        st.error("Required data files not found. Please ensure movie_dict.pkl and similarity.pkl are present.")
        return None, None

# Page configuration
st.set_page_config(
    page_title="Movie-Mate",
    page_icon="🎬",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #FF6B6B;
        text-align: center;
        margin-bottom: 2rem;
    }
    .movie-title {
        font-size: 1.2rem;
        font-weight: bold;
        text-align: center;
        margin-top: 0.5rem;
    }
    .recommendation-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🎬 Movie-Mate</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #666;'>Discover your next favorite movie with AI-powered recommendations</p>", unsafe_allow_html=True)

# Load data
movies, similarity = load_data()

if movies is not None and similarity is not None:
    # Movie selection
    movie_list = movies['title'].values
    selected_movie = st.selectbox(
        "Select a movie you like:",
        movie_list,
        help="Choose a movie to get personalized recommendations"
    )
    
    # Recommend button
    if st.button("🎯 Show Recommendations", type="primary"):
        with st.spinner("Finding perfect movies for you..."):
            names, posters = recommend(selected_movie)
        
        if names:
            st.markdown('<div class="recommendation-container">', unsafe_allow_html=True)
            st.subheader(f"🎭 Movies similar to '{selected_movie}':")
            
            # Display recommendations in columns
            cols = st.columns(5)
            for idx, (name, poster) in enumerate(zip(names, posters)):
                with cols[idx]:
                    if poster:
                        st.image(poster, use_column_width=True)
                    else:
                        st.image("https://via.placeholder.com/300x450.png?text=No+Poster", use_column_width=True)
                    st.markdown(f'<p class="movie-title">{name}</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.error("Unable to generate recommendations. Please try another movie.")
else:
    st.error("Unable to load movie data. Please check the data files.")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #888; padding: 2rem;'>
        <p>Made with ❤️ using Streamlit and Machine Learning</p>
        <p>Data provided by <a href='https://www.themoviedb.org/' target='_blank'>TMDb</a></p>
    </div>
    """,
    unsafe_allow_html=True
)