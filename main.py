"""Main module for Spotify playlist downloader and metadata enhancer."""

import spotify.auth as auth
import spotify.api as api
import downloader.mp3_downloader as mp3_downloader
import metadata.enhancer as enhancer

def main():
    """Main function to authenticate Spotify client, fetch track data,
    download track, and enhance metadata."""
    # Authenticate and get Spotify API client
    spotify_client = auth.authenticate()
    
    # Prompt for track URL
    track_url = input("Enter Spotify track URL: ")
    
    # Fetch track data
    track_data = api.get_track_data(spotify_client, track_url.split('/')[-1].split('?')[0])
    # Download MP3 file
    mp3_file = mp3_downloader.download_track(track_data['url'],track_data)
    
    # Enhance metadata
    enhancer.enhance_metadata(mp3_file, track_data)

if __name__ == "__main__":
    main()
