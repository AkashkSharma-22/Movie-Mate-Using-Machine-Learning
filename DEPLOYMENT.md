# Deployment Guide

## Overview

This guide covers multiple deployment options for Movie-Mate, from local development to cloud platforms.

## Local Development

### Prerequisites
- Python 3.7+
- pip package manager
- Git

### Quick Setup
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

# Set environment variables
cp .env.example .env
# Edit .env with your TMDb API key

# Run application
streamlit run movie_mate.py
```

## Heroku Deployment

### Prerequisites
- Heroku CLI installed
- Git repository initialized
- Heroku account

### Steps

1. **Install Heroku CLI**
   ```bash
   # macOS
   brew install heroku/brew/heroku
   
   # Windows
   winget install Heroku.HerokuCLI
   
   # Ubuntu
   sudo snap install --classic heroku
   ```

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku App**
   ```bash
   heroku create your-movie-mate-app
   ```

4. **Set Environment Variables**
   ```bash
   heroku config:set API_KEY=your_tmdb_api_key
   heroku config:set MOVIE_DICT_ID=your_google_drive_id
   heroku config:set SIMILARITY_ID=your_google_drive_id
   ```

5. **Deploy**
   ```bash
   git add .
   git commit -m "Initial Heroku deployment"
   git push heroku main
   ```

6. **Open Application**
   ```bash
   heroku open
   ```

## Render Deployment

### Prerequisites
- GitHub account
- Render account

### Steps

1. **Push to GitHub**
   ```bash
   git remote add origin https://github.com/yourusername/Movie-Mate.git
   git add .
   git commit -m "Initial commit"
   git push -u origin main
   ```

2. **Connect to Render**
   - Go to [Render Dashboard](https://dashboard.render.com)
   - Click "New" → "Web Service"
   - Connect your GitHub repository
   - Use the following settings:
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `streamlit run movie_mate.py --server.port=10000 --server.address=0.0.0.0`

3. **Set Environment Variables**
   - Add in Render dashboard:
     - `API_KEY`: Your TMDb API key
     - `MOVIE_DICT_ID`: Google Drive file ID
     - `SIMILARITY_ID`: Google Drive file ID

4. **Deploy**
   - Render will automatically deploy on push to main branch

## AWS EC2 Deployment

### Prerequisites
- AWS account
- EC2 instance (Ubuntu 20.04+)
- Security group configured (ports 22, 8501)

### Steps

1. **Launch EC2 Instance**
   ```bash
   # SSH into instance
   ssh -i your-key.pem ubuntu@your-ec2-ip
   ```

2. **Install Dependencies**
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install python3-pip python3-venv git -y
   ```

3. **Setup Application**
   ```bash
   git clone https://github.com/yourusername/Movie-Mate.git
   cd Movie-Mate
   
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Set Environment Variables**
   ```bash
   export API_KEY=your_tmdb_api_key
   export MOVIE_DICT_ID=your_google_drive_id
   export SIMILARITY_ID=your_google_drive_id
   ```

5. **Run with systemd**
   ```bash
   sudo nano /etc/systemd/system/movie-mate.service
   ```

   Add:
   ```ini
   [Unit]
   Description=Movie-Mate Streamlit App
   After=network.target

   [Service]
   Type=simple
   User=ubuntu
   WorkingDirectory=/home/ubuntu/Movie-Mate
   Environment=PATH=/home/ubuntu/Movie-Mate/venv/bin
   Environment=API_KEY=your_tmdb_api_key
   ExecStart=/home/ubuntu/Movie-Mate/venv/bin/streamlit run movie_mate.py --server.port=8501 --server.address=0.0.0.0
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

6. **Start Service**
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl start movie-mate
   sudo systemctl enable movie-mate
   ```

## Docker Deployment

### Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Build and Run
```bash
# Build image
docker build -t movie-mate .

# Run container
docker run -p 8501:8501 -e API_KEY=your_key movie-mate
```

## Environment Variables Reference

| Variable | Description | Required |
|----------|-------------|----------|
| `API_KEY` | TMDb API key | Yes |
| `MOVIE_DICT_ID` | Google Drive file ID for movie_dict.pkl | No |
| `SIMILARITY_ID` | Google Drive file ID for similarity.pkl | No |
| `PORT` | Server port (default: 8501) | No |

## Monitoring and Logs

### Streamlit Logs
```bash
# View logs
streamlit logs

# Check service status
sudo systemctl status movie-mate
```

### Health Check
Add this endpoint to your application:
```python
import streamlit as st

if st.experimental_get_query_params().get('health'):
    st.write("OK")
    st.stop()
```

## Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Find process using port
   sudo lsof -i :8501
   # Kill process
   sudo kill -9 PID
   ```

2. **Memory Issues**
   - Use smaller pickle files
   - Increase instance memory
   - Use memory-efficient data structures

3. **API Rate Limits**
   - Implement caching
   - Add retry logic
   - Use multiple API keys

### Performance Optimization

1. **Enable Caching**
   ```python
   @st.cache_data
   def load_data():
       return pd.read_pickle('movie_dict.pkl')
   ```

2. **Use CDN for Static Files**
   - Host pickle files on CDN
   - Use TMDb's CDN for images

3. **Database Optimization**
   - Consider using SQLite for better performance
   - Implement lazy loading for large datasets