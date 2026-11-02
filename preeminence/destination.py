import time

import requests
from spotipy.exceptions import SpotifyException

from .auth import Authorization
from .source import SourceTracks


class TrackTerminus:

    def __init__(self):
        self.user_id = SourceTracks().user_id
        self.sp = Authorization().authorization_code_flow()
        self.access_token = Authorization().client_credentials_flow()


    def create_playlists(self, playlists):

        created_playlists_ids = {}
        url = "https://api.spotify.com/v1/me/playlists"

        for name, description in playlists.items():
            payload = {
                "name":name,
                "public":False,
                "collaborative":False,
                "description":description,
            }

            headers = {
                "Authorization": f"Bearer {self.access_token}",
                "Content-Type": "application/json"
            }

            while True:

                response = requests.post(
                    headers=headers,
                    data=payload,
                    url=url
                )

                if response.status_code == 429:
                    retry_after = int(response.headers.get("Retry-After", 5))
                    print(f"retrying playlist {name} creation in {retry_after} seconds")
                    time.sleep(retry_after)
                    continue

                response.raise_for_status()
                response_data = response.json()

                created_playlists_ids[name] = response_data.get("id")
                break

            time.sleep(1)

        return created_playlists_ids
            
    def add_to_playlists(self):
        pass