import itertools
import time

from .auth import Authorization
from .source import SourceTracks


class TrackTerminus:

    def __init__(self, track_details, create_playlists):
        self.user_id = SourceTracks().user_id
        self.sp = Authorization().authorization_code_flow()
        self.previous_tracks_details: dict = track_details
        self.playlists: dict = create_playlists

    def create_playlists(self):

        for (name, description), (previous_playlist_id, track_uris) in zip(
            self.playlists.items(), self.previous_tracks_details.items()
        ):
            if not track_uris:
                print(f"skipping playlist ID: {previous_playlist_id}: No tracks found")
                continue

            playlist = self.sp.user_playlist_create(
                user=self.user_id,
                name=name,
                public=False,
                description=description
            )

            if playlist:
                playlist_id = playlist.get("id")
                print(f"playlist '{name}' created. Populating tracks ...")

                time.sleep(2)

                self.populate_playlist(
                    playlist_id=playlist_id,
                    track_uris=track_uris,
                    playlist_name=name
                )
                

    def populate_playlist(self, playlist_id, track_uris, playlist_name):

        for batch in itertools.batched(track_uris, 100):
            self.sp.playlist_add_items(
                playlist_id=playlist_id,
                items=list(batch)
            )

            return f"successfully populated '{playlist_name}' (ID:{playlist_id})"


            
    