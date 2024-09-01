"""
This module implements a Flask server for handling Spotify OAuth authentication,
downloading tracks, and enhancing metadata for MP3 files.
"""

import os
import logging
from flask import Flask, request, render_template, redirect, url_for, session, jsonify, send_file
from dotenv import load_dotenv
import spotify.auth as auth
import spotify.api as api
import downloader.mp3_downloader as mp3_downloader
import metadata.enhancer as enhancer
from downloader.youtube_downloader import YouTubeVideoNotFoundError


load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']

logging.basicConfig(level=logging.INFO)


@app.route('/')
def index():
    """Render the index page."""
    return render_template('index.html')

@app.route('/initiate_auth', methods=['POST'])
def initiate_auth():
    track_url = request.form['track_url']
    session['track_url'] = track_url
    auth_url = auth.get_auth_url()
    return jsonify({'auth_url': auth_url})

@app.route('/callback')
def callback():
    """Handles the Spotify OAuth callback and exchanges the 
                authorization code for an access token."""
    code = request.args.get('code')
    token_info = auth.retrieve_token(code)
    if token_info:
        session['token'] = token_info['access_token']
        return render_template('download.html')
    else:
        return "Authorization failed."

@app.route('/download_page')
def download_page():
    if 'token' not in session or 'track_url' not in session:
        return redirect(url_for('index'))
    return render_template('download.html')

@app.route('/download', methods=['POST'])
def download():
    if 'token' not in session or 'track_url' not in session:
        return jsonify({'error': 'Not authenticated or missing track URL'}), 401

    track_url = session['track_url']
    
    # Authenticate and get Spotify API client using the stored token
    spotify_client = auth.get_spotify_client(session['token'])
    
    # Fetch track data
    track_data = api.get_track_data(spotify_client, track_url.split('/')[-1].split('?')[0])
    
    # Download MP3 file
    try:
        mp3_file = mp3_downloader.download_track(track_data)
        # Enhance metadata
        enhancer.enhance_metadata(mp3_file, track_data)
        return send_file(mp3_file, as_attachment=True, download_name=f"{track_data['name']}.mp3")
    except YouTubeVideoNotFoundError as e:
        return jsonify({'error': str(e)}), 404
    except IOError as e:
        return jsonify({'error': f"File operation error: {str(e)}"}), 500
    except ValueError as e:
        return jsonify({'error': f"Value error: {str(e)}"}), 400
    except Exception as e:
        logging.error("Unexpected error: %s", str(e))
        return jsonify({'error': "An unexpected error occurred"}), 500

if __name__ == "__main__":
    app.run(port=8888)  # Ensure this matches your redirect URI