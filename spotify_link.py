import spotipy
import os

appdata_dir = os.path.join(os.environ['APPDATA'], 'NotifyCache')
if not os.path.exists(appdata_dir):
    os.makedirs(appdata_dir)

client_id = "159e8fc204a64261806d40e85c4fff15"
client_secret = "7bcf5c5acf924ec0b4ae46df86662153"
redirect_uri = "http://localhost:8888/callback/"
auth_manager = spotipy.SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    cache_path=os.path.join(appdata_dir, "spotipy.cache"),
    scope="user-read-currently-playing"
)
sp = spotipy.Spotify(auth_manager=auth_manager)
results = sp.current_user_playing_track()
