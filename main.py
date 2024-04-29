import spotipy
from spotipy.oauth2 import SpotifyOAuth


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/",
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET_KEY",
        show_dialog=True,
        cache_path="Token.txt",
        username="YOUR_USERNAME"
    )
)


user_id = sp.current_user()["id"]

artis = input("Masukkan Nama Artis : ")


result = sp.search(q=f"artist:{artis}",type="track", limit=50, market="ID")
list_result = result["tracks"]["items"]

list_lagu = []
song_uri = []
for lagu in list_result:
    if lagu["name"] not in list_lagu:
        list_lagu.append(lagu["name"])
        song_uri.append(lagu["uri"])

print(list_lagu)

playlist = sp.user_playlist_create(user=user_id,name=f"{artis} Top {len(list_lagu)} ", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uri)
