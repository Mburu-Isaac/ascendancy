import itertools
import json
import time
from pathlib import Path

import requests


class TrackTerminus:

    def __init__(self, track_details, create_playlists, sp):

        root_folder = Path(__file__).resolve().parent.parent

        cache = root_folder/".cache"

        if cache.exists():
            with cache.open("r") as file:
                token_data = json.load(file)

                access_token = token_data.get("access_token")

        
        self.access_token = access_token
        

        self.sp = sp
        self.previous_tracks_details: dict = track_details
        self.playlists: dict = create_playlists


    def create_playlists(self):

        url = "https://api.spotify.com/v1/me/playlists"

        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

        for (name, description), (previous_playlist_id, track_uris) in zip(
            self.playlists.items(), self.previous_tracks_details.items()
        ):
            if not track_uris:
                print(f"skipping playlist ID: {previous_playlist_id}: No tracks found")
                continue

            payload = {
                "name": name,
                "description":description,
                "public": False
            }

            response = requests.post(
                url=url,
                headers=headers,
                json=payload
            )

            if response.status_code in [200, 201]:

                playlist = response.json()
                playlist_id = playlist.get("id")

                print(f"playlist '{name}' created. Populating tracks ...")

                time.sleep(3)

                self.populate_playlist(
                    playlist_id=playlist_id,
                    track_uris=track_uris,
                    playlist_name=name
                )

            else:
                print(f"Failed to create playlist {name}. Error {response.status_code} - {response.text}")
                

    def populate_playlist(self, playlist_id, track_uris, playlist_name):

        for batch in itertools.batched(track_uris, 100):
            self.sp.playlist_add_items(
                playlist_id=playlist_id,
                items=list(batch)
            )

            return f"successfully populated '{playlist_name}' (ID:{playlist_id})"

        time.sleep(2)


            
    