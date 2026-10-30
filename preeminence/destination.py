from spotipy.exceptions import SpotifyException

from .auth import Authorization
from .source import SourceTracks


class TrackTerminus:

    def __init__(self):
        self.user_id = SourceTracks().user_id
        self.sp = Authorization().authorization_code_flow()

    def create_playlist(self, playlists):

        for name, description in playlists.items():
            try:
                new_playlist = self.sp.user_playlist_create(
                    user=self.user_id,
                    name=name,
                    public=False,
                    collaborative=False,
                    description=description,
                )
                if new_playlist:
                    print(
                        f"playlist {new_playlist["name"]}:{new_playlist["description"]}created"
                    )
                    return new_playlist.get("id")

            except SpotifyException as e:
                print(f"playlist creation failed: {e}")


track_destination = TrackTerminus()
print(track_destination.user_id)
