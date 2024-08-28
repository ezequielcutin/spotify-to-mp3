# Spotify Song to MP3 Downloader with Metadata Enhancement

## Overview

This project allows you to download an MP3 file from a Spotify song and enhance its metadata with information such as track title, artist, album, and cover art.

## Features

- **Spotify API Integration**: Securely retrieve song data and track information using OAuth authentication.
- **MP3 Downloading**: Download MP3 files from the provided Spotify song URLs.
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
    git clone https://github.com/ezequielcutin/spotify-to-mp3.git
    cd spotify-to-mp3
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
    SECRET_KEY='your_secret_key'
    ```

## Usage

1. **Run the callback server**:
    ```sh
    python callback_server.py
    ```

2. **Open your browser and navigate to**:
    ```sh
    http://127.0.0.1:8888
    ```

3. **Follow the prompts to authenticate with Spotify and download the song**.

## Project Structure

```
├── callback_server.py
├── main.py
├── requirements.txt
├── .env
├── README.md
├── spotify/
│   ├── __init__.py
│   ├── auth.py
│   └── api.py
├── downloader/
│   ├── __init__.py
│   └── mp3_downloader.py
├── metadata/
│   ├── __init__.py
│   └── enhancer.py
├── static/
│   ├── style.css
│   └── js/
│       ├── mode-toggle.js
│       ├── form-handler.js
│       └── download.js
├── templates/
│   ├── index.html
│   └── download.html
└── tests/
    ├── __init__.py
    └── test_track_download.py # Add more test files as needed
```


## Architecture

This project follows a modular architecture, separating concerns into different components:

1. **Spotify Integration**: The `spotify` module handles authentication and API interactions with Spotify.
2. **Downloader**: The `downloader` module is responsible for downloading MP3 files from URLs.
3. **Metadata Enhancement**: The `metadata` module enhances the downloaded MP3 files with track information and cover art.
4. **Web Interface**: Flask is used to create a user-friendly web interface, with templates and static files for the frontend.
5. **Testing**: A dedicated `tests` directory contains unit tests to ensure the reliability of key components.

## Security Considerations

- Spotify API credentials are stored securely in a `.env` file, which is not tracked by version control.
- OAuth 2.0 is used for secure authentication with the Spotify API.
- User sessions are managed securely using Flask's session management.

## Scalability

The modular design of this project allows for easy scalability:

- Additional features can be added by creating new modules or extending existing ones.
- The separation of concerns allows for easy maintenance and updates to individual components.
- The use of asynchronous operations in JavaScript enables efficient handling of multiple requests.

## Future Enhancements

- More responsibe webpage.
- Accessing Google/Youtube APIs for longer song duration (currently we only get 30 second preview due to Spotify API rules).
- Implement playlist downloading functionality.
- Add support for other music streaming platforms.
- Integrate a caching mechanism to improve performance for frequently accessed tracks.
- Implement user accounts and personalized playlists.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Spotipy](https://spotipy.readthedocs.io/) for Spotify API integration
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Mutagen](https://mutagen.readthedocs.io/) for audio metadata manipulation
- [Spotify Web API](https://developer.spotify.com/documentation/web-api/) for the Spotify API

