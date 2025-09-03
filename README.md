# 🎬 Movie-Mate

A powerful, AI-driven movie recommendation system built with Streamlit and machine learning. Get personalized movie recommendations based on your favorite films using advanced collaborative filtering and content-based algorithms.

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![TMDb](https://img.shields.io/badge/TMDb-API-orange.svg)

## ✨ Features

- **🤖 Smart Recommendations**: AI-powered movie suggestions using machine learning algorithms
- **🎨 Real Posters & Ratings**: Fetches actual movie posters and ratings from TMDb API
- **📱 Responsive Design**: Clean, modern web interface that works on all devices
- **⚡ Fast Performance**: Optimized algorithms for instant recommendations
- **🔄 Offline Fallback**: Smart fallback system when API is unavailable
- **🎯 Accurate Results**: Uses both collaborative filtering and content-based filtering
- **📊 Rich Metadata**: Detailed movie information including cast, ratings, and genres

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- TMDb API key (free from [TMDb](https://www.themoviedb.org/settings/api))

### Installation

#### Method 1: One-Click Setup (Recommended)
```bash
# Clone and setup
git clone https://github.com/yourusername/Movie-Mate.git
cd Movie-Mate
chmod +x setup.sh
./setup.sh
```

#### Method 2: Manual Setup
```bash
# Clone repository
git clone https://github.com/yourusername/Movie-Mate.git
cd Movie-Mate

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your TMDb API key

# Run the application
streamlit run app.py
```

### Environment Setup

Create a `.env` file in the project root:

```bash
# Required
API_KEY=your_tmdb_api_key_here

# Optional - Google Drive IDs for data files
MOVIE_DICT_ID=1LiCe2ZG552tjBztNSHRBtBKSkOdQUaEQ
SIMILARITY_ID=1O8daZuVfRh8vUukVWdyS23NPghrj2kbd
```

**Get your TMDb API key**: [TMDb API Settings](https://www.themoviedb.org/settings/api)

## 🎯 Usage

1. **Open the app** at `http://localhost:8501`
2. **Select a movie** from the dropdown menu (5000+ movies available)
3. **Click "Show Recommendations"** to get 5 personalized suggestions
4. **Explore recommendations** with real posters, ratings, and detailed info

### Demo
![Demo GIF](https://via.placeholder.com/800x400.png?text=Demo+GIF+Placeholder)

## 🛠️ Tech Stack

### Core Technologies
- **Frontend**: Streamlit
- **Backend**: Python 3.7+
- **ML Libraries**: Scikit-learn, Pandas, NumPy
- **API**: TMDb API for real-time movie data
- **Data Storage**: Pickle files for ML models

### Development Tools
- **Package Management**: pip
- **Environment**: python-dotenv
- **HTTP Client**: requests
- **Image Processing**: PIL/Pillow

## 📁 Project Structure

```
Movie-Mate/
├── 📁 app.py                    # Main Streamlit application
├── 📁 requirements.txt          # Python dependencies
├── 📁 .env.example             # Environment variables template
├── 📁 .gitignore               # Git ignore rules
├── 📁 README.md                # Project documentation
├── 📁 LICENSE                   # MIT License
├── 📁 CONTRIBUTING.md          # Contribution guidelines
├── 📁 API_DOCUMENTATION.md     # TMDb API documentation
├── 📁 DEPLOYMENT.md            # Deployment guide
├── 📁 setup.sh                 # Automated setup script
├── 📁 Procfile                 # Heroku deployment config
├── 📁 render.yaml              # Render deployment config
├── 📁 setup.sh                 # Setup script
├── 📁 movie_dict.pkl           # Movie data (auto-downloaded)
├── 📁 similarity.pkl           # Similarity matrix (auto-downloaded)
├── 📁 movies.pkl              # Additional movie data
└── 📁 archive/                # Raw data files
    ├── tmdb_5000_credits.csv
    └── tmdb_5000_movies.csv
```

## 🚀 Deployment Options

### ☁️ Cloud Platforms

#### Heroku (One-Click)
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

#### Render (Recommended)
1. Fork this repository
2. Connect to [Render](https://render.com)
3. Deploy automatically with `render.yaml`

#### AWS EC2
```bash
# Follow detailed guide in DEPLOYMENT.md
```

#### Google Cloud Platform
```bash
# Follow detailed guide in DEPLOYMENT.md
```

### 🐳 Docker
```bash
# Build and run with Docker
docker build -t movie-mate .
docker run -p 8501:8501 -e API_KEY=your_key movie-mate
```

## 🔧 Development

### Setup Development Environment
```bash
# Install development dependencies
pip install -r requirements.txt
pip install black flake8 pytest

# Run code formatting
black .

# Run linting
flake8 .

# Run tests
pytest
```

### Adding New Features
1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Make changes and test thoroughly
4. Run tests: `pytest`
5. Commit changes: `git commit -m 'Add amazing feature'`
6. Push to branch: `git push origin feature/amazing-feature`
7. Open a Pull Request

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Quick Contributing Guide
- 🐛 **Bug Reports**: Use GitHub Issues with detailed reproduction steps
- ✨ **Feature Requests**: Open an issue to discuss before implementation
- 🔧 **Code Contributions**: Follow the development setup above
- 📖 **Documentation**: Help improve our docs and examples

## 📊 Dataset Information

### Source
- **Dataset**: TMDb 5000 Movies Dataset
- **Size**: 5000+ movies with full metadata
- **Features**: Title, genres, keywords, cast, crew, ratings, etc.
- **Format**: CSV and processed pickle files

### Data Processing
1. **Data Cleaning**: Removed duplicates, handled missing values
2. **Feature Engineering**: Extracted keywords, genres, cast
3. **Similarity Calculation**: Cosine similarity between movies
4. **Model Training**: Collaborative filtering + content-based filtering

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[TMDb](https://www.themoviedb.org/)** for providing the amazing movie database API
- **[Streamlit](https://streamlit.io/)** for the incredible web framework
- **[Kaggle](https://www.kaggle.com/)** for the movie dataset
- All contributors and users who made this project possible

## 📞 Support

### Getting Help
- 📖 **Documentation**: Check [API_DOCUMENTATION.md](API_DOCUMENTATION.md) and [DEPLOYMENT.md](DEPLOYMENT.md)
- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/yourusername/Movie-Mate/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/yourusername/Movie-Mate/discussions)
- 📧 **Email**: For security issues, email directly

### Common Issues
1. **API Key Issues**: Ensure your TMDb API key is valid
2. **Memory Errors**: Use smaller instance for deployment
3. **Port Conflicts**: Change port in environment variables
4. **Missing Data**: Data files auto-download on first run

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

[![GitHub stars](https://img.shields.io/github/stars/yourusername/Movie-Mate?style=social)](https://github.com/yourusername/Movie-Mate/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/Movie-Mate?style=social)](https://github.com/yourusername/Movie-Mate/fork)

</div>
