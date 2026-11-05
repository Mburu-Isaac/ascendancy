import time


class EraseTrack:

    def __init__(self, sp, user_id, target_details):
        self.sp = sp
        self.user_id = user_id
        self.target_details: dict = target_details

    def delete_tracks(self):

        for key, value in self.target_details.items():
            self.sp.playlist_remove_all_occurences_of_items(
                user=self.user_id,
                playlist_id=key,
                tracks=value
            )

            print(f"track deleted for ID: {key}")
            time.sleep(5)

        return "END"