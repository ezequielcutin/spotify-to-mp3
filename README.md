# Spotify Song to MP3 Downloader with Metadata Enhancement

## Overview

This project allows you to download an MP3 file from a Spotify song and enhance its metadata with information such as track title, artist, album, and cover art.

## Features

- **Spotify API Integration**: Securely retrieve song data and track information using OAuth authentication.
- **MP3 Downloading**: Download MP3 files from the provided URLs.
- **Metadata Enhancement**: Embed essential information like track title, artist, album, and cover art into MP3 files using the `mutagen` library.
- **Error Handling and Logging**: Comprehensive error handling and logging for debugging purposes.
- **Automated Tests**: Validate the functionality of each component with high test coverage.

## Setup

### Prerequisites

- Python 3.6+
- Spotify Developer Account

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/spotify_song_downloader.git
    cd spotify_song_downloader
    ```

2. **Create a virtual environment and activate it**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up your Spotify API credentials**:
    Create a `.env` file in the root directory and add your Spotify API credentials:
    ```env
    SPOTIPY_CLIENT_ID='your_client_id'
    SPOTIPY_CLIENT_SECRET='your_client_secret'
    SPOTIPY_REDIRECT_URI='your_redirect_uri'
    ```

## Usage

1. **Run the main script**:
    ```sh
    python main.py
    ```

2. **Follow the prompts to authenticate with Spotify and download the song**.

## Project Structure

