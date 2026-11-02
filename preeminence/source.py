from pprint import pprint

from .auth import Authorization

authorization = Authorization()

class SourceTracks:
   
   def __init__(self):
      self.sp = authorization.authorization_code_flow()
      self.user_id = authorization.current_user_id()
      self.user_playlists = []

   def source_playlist_names(self):

      limit = 50
      offset = 0

      while True:
         current_user_playlists = self.sp.current_user_playlists(
            limit=limit,
            offset=offset
         )

         if current_user_playlists:
            items = current_user_playlists["items"]

            if not items:
               break

            self.user_playlists.extend(items)

            offset += limit

            if offset >= current_user_playlists["total"]:
               break

            playlist_names = [playlist["name"] for playlist in self.user_playlists]
            return playlist_names


# source_tracks = SourceTracks()
# print(source_tracks.user_id)


#    def source_playlists_names(self):

#       limit = 50
#       offset = 0

#       while True:
#          current_user_playlists = self.handle_spotify_calls(
#             self.authorize.current_user_playlists,
#             limit=limit,
#             offset=offset
#          )
#          items = current_user_playlists["items"]

#          if not items:
#             break

#          self.user_playlists.extend(items)
#          offset += limit

#          if offset >= current_user_playlists["total"]:
#             break

#       playlist_names = [playlist["name"] for playlist in self.user_playlists]
#       return playlist_names


#    def retrieve_playlist_ids(self, target_playlists):

#       target_indexes = []

#       for target_name in tuple(target_playlists):
#          target_indexes.append(self.source_playlists_names().index(target_name))

#       for index in target_indexes:
#          target_id = self.user_playlists[index].get("id")
#          self.target_playlists_ids.append(target_id)

#    def get_track_uris(self, playlist_id):

#       target_track_uris = {
#          playlist_id:[]
#       }
#       offset = 0
#       limit = 100

#       while True:

#          playlist_item = self.handle_spotify_calls(
#                self.authorize.playlist_items,
#                playlist_id=playlist_id, 
#                limit=limit,
#                offset=offset
#             )

#          for item in playlist_item.get("items"):
#                track_uri = item.get("item").get("uri")

#                target_track_uris[playlist_id].append(track_uri)

#                if not playlist_item.get("next"):
#                   break

#                offset += limit

#       return target_track_uris # start

#    def track_details_retrieval(self):

#       playlist_data = {}

#       for playlist_id in tuple(self.target_playlists_ids):
#          track_uris = self.get_track_uris(playlist_id)
#          playlist_data.update(track_uris)

#       return playlist_data
   


# source = SourceTracks()
# source.retrieve_playlist_ids(
#    target_playlists = ["Nolstagic", "Afro"]
# )
# # source.get_track_details()
# pprint(source.track_details_retrieval())

# # ["OverDrive", "254 spits", "Chill Afro", "Glass Hearts & Wild Fire 🧬👣", "Lukas Graham", "EDM"]