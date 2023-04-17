import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import argparse 

# Set up Spotify credentials
client_id = '287900deaf494c6da36a97b87f0085de'
client_secret = '002554111145409d8f828f98fff8b795'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Define the available sorting variables
SORT_VARS = ['length', 'popularity', 'valence', 'energy', 'bpm']

# Define a function to sort a playlist by a given variable
def sort_playlist(playlist_id, sort_var):
    playlist_tracks = sp.playlist_tracks(playlist_id, fields='items(track(id,name,duration_ms,artists))')['items']
    if sort_var == 'length':
        total_length = sum(track['track']['duration_ms'] for track in playlist_tracks)
        return total_length
    elif sort_var == 'popularity':
        avg_popularity = sum(track['track']['popularity'] for track in playlist_tracks) / len(playlist_tracks)
        return avg_popularity
    elif sort_var == 'valence':
        avg_valence = sum(sp.audio_features(track['track']['id'])[0]['valence'] for track in playlist_tracks) / len(playlist_tracks)
        return avg_valence
    elif sort_var == 'energy':
        avg_energy = sum(sp.audio_features(track['track']['id'])[0]['energy'] for track in playlist_tracks) / len(playlist_tracks)
        return avg_energy
    elif sort_var == 'bpm':
        avg_bpm = sum(sp.audio_features(track['track']['id'])[0]['tempo'] for track in playlist_tracks) / len(playlist_tracks)
        return avg_bpm

