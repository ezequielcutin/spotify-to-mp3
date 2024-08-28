"""
Test module for downloading and enhancing Spotify tracks.
"""
import sys
import os

# Add the parent directory to the system path to access local modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))


import spotify.auth as auth
import spotify.api as api
import downloader.mp3_downloader as mp3_downloader
import metadata.enhancer as enhancer

def test_download_and_enhance(url):
    """Test downloading and enhancing a Spotify track given its URL."""
    # Authenticate and get Spotify API client
    spotify_client = auth.authenticate()
    
    # Extract track ID from the Spotify URL
    track_id = url.split('/')[-1].split('?')[0]
    
    # Fetch track data
    track_data = api.get_track_data(spotify_client, track_id)
    
    # Download MP3 file
    mp3_file = mp3_downloader.download_track(track_data['url'],track_data)
    
    # Enhance metadata
    enhancer.enhance_metadata(mp3_file, track_data)
    
    print(f"Downloaded and enhanced track: {track_data['name']} by {track_data['artist']}")

if __name__ == "__main__":
    spotify_url = input("Enter Spotify track URL: ")
    test_download_and_enhance(spotify_url)
