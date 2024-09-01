from googleapiclient.discovery import build
import yt_dlp as youtube_dl
import os
from dotenv import load_dotenv

load_dotenv()




def search_youtube(query, api_key):
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

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def download_audio(video_id, output_path):
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
    api_key = os.getenv('YOUTUBE_API_KEY')
    query = f"{track_info['name']} {track_info['artist']}"
    video_id = search_youtube(query, api_key)
    if video_id:
        output_path = os.path.join(os.path.expanduser('~/Downloads'), f"{track_info['name']}_{track_info['artist']}.%(ext)s")
        download_audio(video_id, output_path)
        return output_path.replace('%(ext)s', 'mp3')
    else:
        raise Exception("No YouTube video found for the track")


if __name__ == "__main__":
    api_key = os.getenv('YOUTUBE_API_KEY')
    query = "Rufus Du Sol Like an Animal"
    video_id = search_youtube(query, api_key)
    
    if video_id:
        output_path = os.path.join(os.path.expanduser('~/Downloads'), f"Rufus_Du_Sol_Like_an_Animal.%(ext)s")
        try:
            download_audio(video_id, output_path)
            print(f"Successfully downloaded: {output_path.replace('%(ext)s', 'mp3')}")
        except Exception as e:
            print(f"Error downloading audio: {str(e)}")
            print("Full error:")
            import traceback
            traceback.print_exc()
    else:
        print("Failed to find the video.")