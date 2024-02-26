import spotipy

client_id = "159e8fc204a64261806d40e85c4fff15"
client_secret = "7bcf5c5acf924ec0b4ae46df86662153"
redirect_uri = "http://localhost:8888/callback/"
auth_manager = spotipy.SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope="user-read-currently-playing"
)
sp = spotipy.Spotify(auth_manager=auth_manager)
results = sp.current_user_playing_track()
