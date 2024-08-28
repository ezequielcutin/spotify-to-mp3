"""
This module handles downloading MP3 files from given URLs.
"""

import os
import requests

def download_track(track_url, track_info):
    """
    Downloads an MP3 file from the given URL and saves it to the downloads directory.
    
    Args:
        track_url (str): The URL of the MP3 file to download.
        track_info (dict): Dictionary containing track information (name and artist).

    Returns:
        str: The file path of the downloaded MP3 file.
    """
    response = requests.get(track_url, timeout=100)  # Added timeout argument
    if response.status_code == 200:
        # Create a filename using the track name and artist
        file_name = f"{track_info['name']}_{track_info['artist']}.mp3"
        file_name = os.path.join(os.path.expanduser('~/Downloads'), file_name)  # Save to Downloads folder
        with open(file_name, 'wb') as file:
            file.write(response.content)
        return file_name
    else:
        raise requests.exceptions.HTTPError(f"Failed to download track: {response.status_code}")
