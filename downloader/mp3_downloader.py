"""
This module handles downloading MP3 files from given URLs.
"""

import os
from .youtube_downloader import search_youtube, download_audio

def download_track(track_info):
    """
    Downloads an MP3 file from the given URL and saves it to the downloads directory.
    
    Args:
        track_info (dict): Dictionary containing track information (name and artist).

    Returns:
        str: The file path of the downloaded MP3 file.
    """
    api_key = os.getenv('YOUTUBE_API_KEY')
    video_id = search_youtube(track_info['query'], api_key)
    if video_id:
        output_path = os.path.join(os.path.expanduser('~/Downloads'), f"{track_info['name']}_{track_info['artist']}.%(ext)s")
        download_audio(video_id, output_path)
        return output_path.replace('%(ext)s', 'mp3')
    else:
        raise Exception("No YouTube video found for the track")
