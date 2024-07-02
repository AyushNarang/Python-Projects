from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = ""
SPOTIFY_CLIENT_SECRET = ""
SPOTIFY_REDIRECT_URI = "http://example.com"

year = input("Enter the year of songs would you like in your playlist (YYYY-MM-DD): ")

billboard_url = "https://www.billboard.com/charts/hot-100/"

response = requests.get(f"{billboard_url}/{year}/")
billboard_content = response.text

soup = BeautifulSoup(billboard_content, 'html.parser')

songs_list = soup.select("li ul li h3")
songs = [song.getText().strip() for song in songs_list]

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",
                                               client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=SPOTIFY_REDIRECT_URI,
                                               show_dialog=True,
                                               cache_path=".cache",
                                               username="Ayush Narang"))

user_id = sp.current_user()["id"]
uri_list = []
year_check = year.split("-")[0]

for song in songs:
    result = sp.search(q=f"track:{song} year:{year_check}", type="track")
    try:
        uri = result['tracks']['items'][0]['uri']
        uri_list.append(uri)
    except IndexError:
        print(f"{song} does not exist on Spotify. Skipped.")

playlist_response = sp.user_playlist_create(name=f"{year} Billboard Top 100", public=False, user=user_id,
                                            description="Playlist containing the Billboard Top 100 "
                                                        "songs from the particular day")
playlist_id = playlist_response["id"]

playlist_add_response = sp.playlist_add_items(playlist_id=playlist_id, items=uri_list)
print(playlist_add_response)