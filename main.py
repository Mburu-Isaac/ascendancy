
from preeminence.destination import TrackTerminus
from preeminence.divest import EraseTrack
from preeminence.source import SourceTracks

playlists_to_create = {
    "Nostalgic": "first",
    "Afro Reclaimed": "two",
    "OverDrive Reclaimed": "🙂 - the unspeakable mind.",
    "254": "Kenyan spits Reclaimed",
    "Chill Afro Reclaimed": "four",
    "Glass Hearts & Wild Fire 🧬": "Delicate emotion meets uncontrollable passion",
    "Lukas Graham Reclaimed": "seven",
    "EDM Reclaimed": "final",
}

target_playlists = [
    "Nolstagic",
    "Afro",
    "OverDrive",
    "254 spits",
    "Chill Afro",
    "Glass Hearts & Wild Fire 🧬👣",
    "Lukas Graham",
    "EDM",
]

# source playlists' data
source = SourceTracks()
playlist_track_details = source.retrieve_track_details(
    target_playlists=target_playlists
)

# create and populate
destination = TrackTerminus(
    track_details=playlist_track_details, create_playlists=playlists_to_create
)
create_populate = destination.create_playlists()
print(create_populate)

# delete track data
divest = EraseTrack(
    sp=destination.sp,
    user_id=destination.user_id,
    target_details=playlist_track_details
)
print(divest.delete_tracks())


