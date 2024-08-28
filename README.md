# Spotify Playlist to MP3 Downloader with Metadata Enhancement

## Overview

This project allows you to download MP3 files from a Spotify playlist and enhance their metadata with information such as track title, artist, album, and cover art.

## Features

- **Spotify API Integration**: Securely retrieve playlist data and track information using OAuth authentication.
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
    git clone https://github.com/yourusername/spotify_playlist_downloader.git
    cd spotify_playlist_downloader
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

2. **Follow the prompts to authenticate with Spotify and download the playlist**.

## Project Structure

```
spotify_playlist_downloader/
├── main.py
├── spotify/
│   ├── __init__.py
│   ├─�� auth.py
│   ├── api.py
├── downloader/
│   ├── __init__.py
│   ├── mp3_downloader.py
├── metadata/
│   ├── __init__.py
│   ├── enhancer.py
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_api.py
│   ├── test_mp3_downloader.py
│   ├── test_enhancer.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Testing

Run the tests to validate the functionality of each component:
```sh
pytest
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Spotipy](https://spotipy.readthedocs.io/en/2.16.1/) - A lightweight Python library for the Spotify Web API.
- [Mutagen](https://mutagen.readthedocs.io/en/latest/) - A Python module to handle audio metadata.
