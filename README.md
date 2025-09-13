# 🎬 Movie-Mate

A smart movie recommendation system that uses machine learning to suggest movies based on your preferences. Built with Python and Streamlit for a seamless user experience.

## ✨ Features

- **Intelligent Recommendations**: ML-powered movie suggestions using content-based filtering
- **Real-time Data**: Fetches actual movie posters and ratings from TMDb API
- **Responsive Design**: Clean, modern interface that works on all devices
- **Fast Performance**: Optimized algorithms for instant recommendations
- **Easy Setup**: Simple installation with minimal configuration

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- TMDb API key (free from [TMDb](https://www.themoviedb.org/settings/api))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AkashkSharma-22/Movie-Mate-Using-Machine-Learning.git
   cd Movie-Mate-Using-Machine-Learning
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your TMDb API key
   ```

4. **Run the application**
   ```bash
   streamlit run movie_mate.py
   ```

5. **Access the app** at `http://localhost:8501`

## 🎯 Usage

1. Select a movie from the dropdown menu
2. Click "Show Recommendations"
3. Explore personalized movie suggestions with posters and ratings

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python 3.7+
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **API**: TMDb API for movie data
- **Data Processing**: Pickle files for ML models

## 🐳 Docker Support

Build and run with Docker:

```bash
# Build image
docker build -t movie-mate .

# Run container
docker run -p 8501:8501 -e API_KEY=your_tmdb_api_key movie-mate
```

## 📁 Project Structure

```
Movie-Mate/
├── movie_mate.py          # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── Dockerfile            # Docker configuration
├── README.md             # Project documentation
├── LICENSE               # MIT License
├── .gitignore           # Git ignore rules
├── .github/             # GitHub workflows
└── archive/             # Raw dataset files
```

## 🔧 Development

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run movie_mate.py
```

### Environment Variables
Create a `.env` file:
```
API_KEY=your_tmdb_api_key_here
```

## 📊 Dataset

Built using the TMDb 5000 Movies dataset, featuring:
- 5,000+ movies with complete metadata
- Genres, keywords, cast, and crew information
- User ratings and popularity scores

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs via GitHub Issues
- Suggest new features
- Submit pull requests

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [TMDb](https://www.themoviedb.org/) for the comprehensive movie database
- [Streamlit](https://streamlit.io/) for the excellent web framework
- The open-source community for inspiration and support
