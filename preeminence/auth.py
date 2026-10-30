import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth


class Authorization:
    
    def __init__(self):
        self.client_id =  os.environ.get("MY_CLIENT_ID")
        self.client_secret = os.environ.get("MY_CLIENT_SECRET")

    def authorization_code_flow(self):
        sp = spotipy.Spotify(
            auth_manager = SpotifyOAuth(
                client_id =self.client_id,
                client_secret = self.client_secret,
                redirect_uri = "https://example.com",
                scope = "playlist-read-private playlist-modify-private playlist-modify-public"
            )
        )
        return sp

    def get_current_user(self):
        current_user = self.authorization_code_flow().current_user()
        return current_user

    def current_user_id(self):
        current_user = self.get_current_user()
        
        if current_user is not None:
            return current_user["id"]

    def client_credentials_flow(self):
        pass

authorization = Authorization()
print(authorization.get_current_user())

        


