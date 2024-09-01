"""Module for enhancing MP3 metadata with track information and cover art."""

import requests
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC

def enhance_metadata(file_path, track_info):
    """Enhances MP3 metadata with track information and cover art."""
    audio = EasyID3(file_path)
    audio['title'] = track_info['name']
    audio['artist'] = track_info['artist']
    audio['album'] = track_info['album']
    audio.save()

    # Download cover art if it doesn't exist in the MP3
    cover_art_url = track_info.get('cover_art')  # Ensure this key exists in track_info
    if cover_art_url:
        response = requests.get(cover_art_url, timeout=10)
        if response.status_code == 200:
            audio = ID3(file_path)
            audio['APIC'] = APIC(
                encoding=3,
                mime='image/jpeg',
                type=3,
                desc='Cover',
                data=response.content
            )
            audio.save()
        else:
            raise requests.HTTPError(f"Failed to download cover art: {response.status_code}")
