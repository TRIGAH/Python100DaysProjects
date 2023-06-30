import requests
from bs4 import BeautifulSoup
from datetime import datetime
import spotipy
import pprint
from spotipy.oauth2 import SpotifyOAuth,SpotifyClientCredentials


CLIENT_ID = "7b47cfefeea54081a45d28ecc312f78c"
CLIENT_SECRET = "ea0deaebb3844f419deccee76cd05a91"

playlist_date = input("Which Year do you want to Travel to? Type the Date in this format YYYY-MM-DD: ")
SPOTIFY_URL = f"https://www.billboard.com/charts/hot-100/{playlist_date}"

scope = "playlist-modify-private"
user_spotify_id = "52zfk36c972mtwvgye6y5xa9b"

all_song_titles = []
all_spotify_track_uris = []

response = requests.get(SPOTIFY_URL)
spotify_html = response.text
soup = BeautifulSoup(spotify_html,"html.parser")
song_titles = soup.select(".c-title.a-no-trucate")
for song_title in song_titles:
    all_song_titles.append(song_title.getText().replace("\t",'').replace("\n",'').strip())

auth_manager = SpotifyClientCredentials()
sp=spotipy.Spotify(auth_manager=auth_manager)
for track_name in all_song_titles:
    try:  
        track = sp.search(q=' track:' + track_name, type='track')
        track_uri = track['tracks']['items'][0]['uri']
    except IndexError:
        pass
    else:        
        all_spotify_track_uris.append(track_uri)

playlist_name = f"{playlist_date} Billboard 100"
auth_manager = SpotifyClientCredentials()
sp_playlist=spotipy.Spotify(auth_manager=auth_manager)

# CREATE SPOTIFY PLAYLIST AND GET ID
# playlist= sp_playlist.user_playlist_create(user_spotify_id,playlist_name,public=False,collaborative=False)
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(playlist['id'])

playlist_id = "5tlTKI54A1U6cPVBps2GWJ"
sp_playlist.user_playlist_add_tracks(user_spotify_id,playlist_id,all_spotify_track_uris)
print(sp_playlist.playlist(playlist_id)['name'])
for key in sp_playlist.playlist_items(playlist_id)['items']:
    print(key['track']['name'])

# print(sp_playlist.user_playlist(user_spotify_id))
# for playlist in sp_playlist.user_playlists('spotify')['items']:
#     print(playlist['name'])



















#Spotify Playlist IDs
# '5tlTKI54A1U6cPVBps2GWJ'
# "1qQTbluSklDvAyJzGUXABO"
# "5n0oNknmg01E3duzi5O9Rj"

    # tracks_bill=f"track: {track_name} year: {playlist_date.split('-')[0]}"
    # print(tracks_bill)

# 
# sp_client = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
# results = sp_client.current_user()
# print(results['id'])

# playlists = sp_playlist.user_playlists(f"{results['id']}")
# print(playlists)

# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp_playlist.next(playlists)
#     else:
#         playlists = None

