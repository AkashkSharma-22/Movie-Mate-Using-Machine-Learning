# API Documentation

## TMDb API Integration

Movie-Mate uses the TMDb (The Movie Database) API to fetch real-time movie information including posters, ratings, and metadata.

### API Endpoints Used

#### 1. Search Movies
- **Endpoint**: `https://api.themoviedb.org/3/search/movie`
- **Method**: GET
- **Parameters**:
  - `api_key`: Your TMDb API key
  - `query`: Movie title to search
  - `include_adult`: false (filter adult content)
  - `page`: 1 (pagination)

#### 2. Movie Details
- **Endpoint**: `https://api.themoviedb.org/3/movie/{movie_id}`
- **Method**: GET
- **Parameters**:
  - `api_key`: Your TMDb API key

#### 3. Configuration
- **Endpoint**: `https://api.themoviedb.org/3/configuration`
- **Method**: GET
- **Parameters**:
  - `api_key`: Your TMDb API key

### Image URLs

Movie posters are fetched using TMDb's image service:
- **Base URL**: `https://image.tmdb.org/t/p/`
- **Size Options**:
  - `w92`: Small thumbnail
  - `w154`: Small
  - `w185`: Medium
  - `w342`: Large
  - `w500`: Extra large
  - `w780`: Maximum quality
  - `original`: Original resolution

### Rate Limiting

TMDb API has the following rate limits:
- **Standard tier**: 40 requests per 10 seconds
- **Exponential backoff**: Automatically applied on rate limit

### Error Handling

The application implements robust error handling for:
- **404 Not Found**: Movie not found in database
- **401 Unauthorized**: Invalid API key
- **429 Too Many Requests**: Rate limiting
- **Network Errors**: Connection timeouts and failures
- **Timeout Errors**: 5-second timeout for API calls

### Fallback Mechanism

When API calls fail, the system uses:
1. **Placeholder Images**: Dynamic placeholder based on movie title
2. **Default Ratings**: 7.0/10 as default rating
3. **Cached Data**: Previous successful API responses
4. **Offline Mode**: Full functionality without API dependency

### Setup Instructions

1. **Get API Key**:
   - Visit [TMDb API](https://www.themoviedb.org/settings/api)
   - Create a free account
   - Generate an API key

2. **Configure Environment**:
   ```bash
   # In .env file
   API_KEY=your_actual_api_key_here
   ```

3. **Test API Connection**:
   ```python
   import requests
   
   api_key = "your_api_key"
   response = requests.get(
       f"https://api.themoviedb.org/3/search/movie",
       params={
           "api_key": api_key,
           "query": "Inception"
       }
   )
   print(response.json())
   ```

### Monitoring

Monitor API usage through:
- TMDb API Dashboard
- Application logs
- Error tracking in Streamlit interface