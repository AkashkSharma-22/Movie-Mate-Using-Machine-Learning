#!/bin/bash

# Movie-Mate Setup Script
# This script automates the setup process for Movie-Mate

set -e  # Exit on any error

echo "🎬 Setting up Movie-Mate..."
echo "================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

print_status "Python 3 found: $(python3 --version)"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    print_error "pip3 is not installed. Please install pip."
    exit 1
fi

print_status "pip3 found: $(pip3 --version)"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    print_status "Creating virtual environment..."
    python3 -m venv venv
else
    print_status "Virtual environment already exists."
fi

# Activate virtual environment
print_status "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
print_status "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
print_status "Installing dependencies..."
pip install -r requirements.txt

# Check if .env file exists
if [ ! -f ".env" ]; then
    print_status "Creating .env file from template..."
    cp .env.example .env
    print_warning "Please edit .env file with your TMDb API key"
else
    print_status ".env file already exists."
fi

# Check if data files exist
if [ ! -f "movie_dict.pkl" ] || [ ! -f "similarity.pkl" ]; then
    print_warning "Data files missing. They will be auto-downloaded on first run."
else
    print_status "Data files found."
fi

# Test the application
print_status "Testing the application..."
python -c "import streamlit; print('Streamlit version:', streamlit.__version__)"

# Create run script
cat > run.sh << 'EOF'
#!/bin/bash
source venv/bin/activate
streamlit run movie_mate.py --server.port=8501 --server.address=0.0.0.0
EOF

chmod +x run.sh

# Create Windows batch file
cat > run.bat << 'EOF'
@echo off
call venv\Scripts\activate
streamlit run movie_mate.py --server.port=8501 --server.address=0.0.0.0
pause
EOF

print_status "Setup complete! 🎉"
echo ""
echo "To run the application:"
echo "1. Edit .env file with your TMDb API key"
echo "2. Run: ./run.sh (Linux/Mac) or run.bat (Windows)"
echo "3. Open http://localhost:8501 in your browser"
echo ""
echo "For help, visit: https://github.com/yourusername/Movie-Mate"
