import os
import logging
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from requests.exceptions import RequestException

# Load environment variables from .env file
load_dotenv()

def authenticate():
    auth_url = get_auth_url()
    print(f"Please navigate here: {auth_url}")
    
    response_url = input("Enter the URL you were redirected to: ")
    code = SpotifyOAuth().parse_response_code(response_url)
    
    token_info = retrieve_token(code)
    access_token = token_info['access_token']
    
    return get_spotify_client(access_token)

def retrieve_token(code):
    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
    redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI')
    
    token_url = 'https://accounts.spotify.com/api/token'
    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
    }

    logging.debug("Payload: %s", payload)
    logging.debug("Client ID: %s", client_id)
    logging.debug("Redirect URI: %s", redirect_uri)
    
    try:
        response = requests.post(token_url, 
                                 data=payload, 
                                 auth=(client_id, client_secret),
                                 timeout=10)  # Add a 10-second timeout
        response.raise_for_status()
    except RequestException as e:
        raise SpotifyAuthError(f"Error retrieving token: {str(e)}") from e
    
    logging.debug("Response status: %s", response.status_code)
    logging.debug("Response content: %s", response.text)
    
    if response.status_code != 200:
        raise SpotifyAuthError(f"Error retrieving token: {response.json()}")
    
    return response.json()

class SpotifyAuthError(Exception):
    """Custom exception for Spotify authentication errors."""

def get_auth_url():
    sp_oauth = SpotifyOAuth(client_id=os.getenv('SPOTIFY_CLIENT_ID'),
                            client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
                            redirect_uri=os.getenv('SPOTIFY_REDIRECT_URI'),
                            scope='user-library-read')
    return sp_oauth.get_authorize_url()

def get_spotify_client(token):
    return spotipy.Spotify(auth=token)