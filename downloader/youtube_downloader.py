"""Module for searching and downloading audio from YouTube videos."""

import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import yt_dlp as youtube_dl
from google.auth.exceptions import GoogleAuthError
from requests.exceptions import RequestException
from dotenv import load_dotenv

load_dotenv()


def search_youtube(query, api_key):
    """
    Search YouTube for a video matching the query.
    Args:
        query (str): The search query.
        api_key (str): YouTube API key.

    Returns:
        str or None: Video ID if found, None otherwise.
    """
    youtube = build('youtube', 'v3', developerKey=api_key)
    # pylint: disable=no-member
    try:
        search_response = youtube.search().list(
            q=query,
            type='video',
            part='id,snippet',
            maxResults=1
        ).execute()

        if search_response['items']:
            video_id = search_response['items'][0]['id']['videoId']
            print(f"Found video ID: {video_id}")
            return video_id
        else:
            print("No videos found.")
            return None

    except (HttpError, GoogleAuthError) as e:
        print(f"YouTube API error occurred: {str(e)}")
        return None
    except RequestException as e:
        print(f"Network error occurred: {str(e)}")
        return None

def download_audio(video_id, output_path):
    """
    Download audio from a YouTube video.
    Args:
        video_id (str): YouTube video ID.
        output_path (str): Path to save the downloaded audio.
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_path,
        'verbose': True  # Add this line
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f'https://www.youtube.com/watch?v={video_id}'])

def get_full_track(track_info):
    """
    Search for and download a track from YouTube.
    Args:
        track_info (dict): Dictionary containing 'name' and 'artist' keys.
    Returns:
        str: Path to the downloaded MP3 file.
    Raises:
        YouTubeVideoNotFoundError: If no matching video is found.
    """
    api_key = os.getenv('YOUTUBE_API_KEY')
    query = f"{track_info['name']} {track_info['artist']}"
    video_id = search_youtube(query, api_key)
    if video_id:
        filename = f"{track_info['name']}_{track_info['artist']}.%(ext)s"
        output_path = os.path.join(os.path.expanduser('~/Downloads'), filename)
        download_audio(video_id, output_path)
        return output_path.replace('%(ext)s', 'mp3')
    else:
        raise YouTubeVideoNotFoundError(
            f"No YouTube video found for '{track_info['name']}' "
            f"by {track_info['artist']}"
        )


class YouTubeVideoNotFoundError(Exception):
    """Exception raised when a YouTube video is not found."""
