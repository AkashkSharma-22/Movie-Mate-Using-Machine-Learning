# 🎬 Movie-Mate

A simple movie recommendation app built with Python and Streamlit. Just pick a movie and get personalized recommendations!

## Quick Start

1. Get your free TMDb API key from [TMDb](https://www.themoviedb.org/settings/api)
2. Clone the repo
3. Install dependencies: `pip install -r requirements.txt`
4. Create `.env` file with your API key: `API_KEY=your_key_here`
5. Run: `streamlit run movie_mate.py`

## Features

- Smart movie recommendations
- Real movie posters and ratings
- Clean, responsive design
- Works on any device

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python 3.7+
- **API**: TMDb for movie data
- **ML**: Content-based filtering

## Usage

Open http://localhost:8501 in your browser, select a movie, and click "Show Recommendations"!

## Docker

```bash
docker build -t movie-mate .
docker run -p 8501:8501 -e API_KEY=your_key movie-mate
```
