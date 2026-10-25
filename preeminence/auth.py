import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth


class Authorization:
    
    def __init__(self):
        self.sp = spotipy.Spotify(
            auth_manager = SpotifyOAuth(
                client_id = os.environ.get("MY_CLIENT_ID"),
                client_secret = os.environ.get("MY_CLIENT_SECRET"),
                redirect_uri = "https://example.com",
                scope = "playlist-read-private"
            )
        )
  
authorization = Authorization()
print(authorization.sp.current_user().get("display_name"))


