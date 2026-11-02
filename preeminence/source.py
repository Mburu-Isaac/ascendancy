from pprint import pprint

from .auth import Authorization

authorization = Authorization()

class SourceTracks:
   
   def __init__(self):
      self.sp = authorization.authorization_code_flow()
      self.user_id = authorization.current_user_id()
      self.user_playlists_details = []

   def source_playlist_details(self):

      self.user_playlists_details = []

      limit = 50
      offset = 0

      while True:
         current_user_playlists = self.sp.current_user_playlists(
            limit=limit,
            offset=offset
         )

         if not current_user_playlists:
            break

         items = current_user_playlists.get("items", [])

         if not items:
            break

         self.user_playlists_details.extend(items)

         offset += limit

         if offset >= current_user_playlists["total"]:
            break

      return self.user_playlists_details

   def retrieve_playlists_ids(self, target_playlists):

      target_playlists_ids = []
      print("system commencing playlists names retrieval process")
      playlist_names = self.source_playlist_details()


      for target_playlist_name in tuple(target_playlists):

         if playlist_names:
            target_playlist_index = playlist_names.index(target_playlist_name)

            target_playlist_id = self.user_playlists_details[target_playlist_index].get("id")
            target_playlists_ids.append(target_playlist_id)
            print(f"{target_playlist_name} id appended to 'target playlist ids' list")

      return target_playlists_ids

   def get_track_uris(self, playlist_id):

      playlist_tracks_data = {
         playlist_id: []
      }

      limit = 100
      offset = 0

      print("Retrieval for track URIs in the target playlists starts now ...")

      while True:
         playlist_item = self.sp.playlist_tracks(
            playlist_id=playlist_id,
            limit=limit,
            offset=offset
         )

         if not playlist_item:
            break

         items = playlist_item.get("items", []) 

         if not items:
            break

         for item in items:
            track = item.get("track")

            if track and item.get("uri"):
               playlist_tracks_data[playlist_id] = item.get("uri")

         if not playlist_item.get("next"):
            break

         offset += limit

      return playlist_tracks_data

   def retrieve_track_details(self, target_playlists):

      playlist_data = {}
      target_playlist_ids = self.retrieve_playlists_ids(
         target_playlists=target_playlists
      )

      for playlist_id in target_playlist_ids:
         track_details = self.get_track_uris(playlist_id)
         playlist_data.update(track_details)

      return playlist_data

 # ["Nolstagic", "Afro","OverDrive", "254 spits", "Chill Afro", "Glass Hearts & Wild Fire 🧬👣", "Lukas Graham", "EDM"]