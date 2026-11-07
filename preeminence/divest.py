import itertools
import time


class EraseTrack:

    def __init__(self, sp, user_id, target_details):
        self.sp = sp
        self.user_id = user_id
        self.target_details: dict = target_details

    def delete_tracks(self):

        for key, value in self.target_details.items():
            for batch in itertools.batched(value, 100):
                self.sp.playlist_remove_all_occurrences_of_items(
                    playlist_id=key,
                    items=list(batch)
                )
                time.sleep(1)

            print(f"tracks deleted for ID: {key}")
            time.sleep(5)

        return "END"