"""Basic tests for Movie-Mate application."""
import os
import sys
import pytest

# Add the parent directory to the path so we can import movie_mate
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_import_movie_mate():
    """Test that we can import the main application."""
    try:
        import movie_mate
        assert True
    except ImportError as e:
        pytest.fail(f"Failed to import movie_mate: {e}")

def test_required_files_exist():
    """Test that required files exist."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    required_files = [
        'movie_mate.py',
        'requirements.txt',
        '.env.example',
        'README.md'
    ]
    
    for file in required_files:
        file_path = os.path.join(base_dir, file)
        assert os.path.exists(file_path), f"Required file {file} does not exist"

def test_environment_variables():
    """Test that environment variables are properly configured."""
    from dotenv import load_dotenv
    
    # Load environment variables from .env.example for testing
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env_example = os.path.join(base_dir, '.env.example')
    
    if os.path.exists(env_example):
        load_dotenv(env_example)
        
        # Check if API_KEY is defined
        api_key = os.getenv('API_KEY')
        assert api_key is not None, "API_KEY should be defined in .env.example"
        assert len(api_key) > 0, "API_KEY should not be empty"