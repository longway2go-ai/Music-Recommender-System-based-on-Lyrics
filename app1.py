# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 22:13:57 2025
@author: koush
"""

import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API credentials
CLIENT_ID = "70a9fb89662f4dac8d07321b259eaad7"
CLIENT_SECRET = "4d6710460d764fbbb8d8753dc094d131"

# Initialize Spotify API
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Function to get album art
def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")
    if results and results["tracks"]["items"]:
        return results["tracks"]["items"][0]["album"]["images"][0]["url"]
    return "C:/Users/koush/anaconda3/Spotify Recommender System/social.png"  # Fallback image

# Recommendation logic
def recommend(song):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music_names = []
    recommended_music_posters = []
    for i in distances[1:6]:
        artist = music.iloc[i[0]].artist
        recommended_music_names.append(music.iloc[i[0]].song)
        recommended_music_posters.append(get_song_album_cover_url(music.iloc[i[0]].song, artist))
    return recommended_music_names, recommended_music_posters

# --------------------- UI ---------------------
st.set_page_config(page_title="Music Recommender", layout="wide")

st.markdown(
    """
    <h1 style='text-align: center; color: #1DB954;'>🎶 Music Recommender (Lyrics Based)</h1>
    <p style='text-align: center; font-size: 18px;'>Discover songs similar to your favorites</p>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """<div style='text-align: center; margin-bottom: 20px;'>
         <img src='https://media.giphy.com/media/JxxkWxHOEDrq0/giphy.gif' width='250'>
       </div>""",
    unsafe_allow_html=True
)

# Load data
music = pickle.load(open('data.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Song selector
music_list = music['song'].values
selected_song = st.selectbox("🎧 Select a song you like:", music_list)

if st.button("🔍 Recommend Me Songs!"):
    st.subheader(f"🎵 Because you like: *{selected_song}*")
    recommended_music_names, recommended_music_posters = recommend(selected_song)
    
    # Display recommendations
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.image(recommended_music_posters[i], use_container_width=True)
            st.caption(recommended_music_names[i])

# Optional: footer
st.markdown(
    "<hr style='margin-top: 40px;'><p style='text-align: center;'>Made with ❤️ using Streamlit & Spotify API by Arnab</p>",
    unsafe_allow_html=True
)