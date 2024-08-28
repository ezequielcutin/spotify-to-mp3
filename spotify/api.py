def get_track_data(spotify_client, track_id):
    """
    Retrieve track data from Spotify.

    Args:
        spotify_client: Authenticated Spotify client.
        track_id (str): Spotify track ID.

    Returns:
        dict: Track name and metadata.
    """
    track = spotify_client.track(track_id)
    return {
        'name': track['name'],
        'artist': track['artists'][0]['name'],
        'url': track['preview_url'],
        'album': track['album']['name'],
        'cover_art': track['album']['images'][0]['url'] if track['album']['images'] else None
    }
