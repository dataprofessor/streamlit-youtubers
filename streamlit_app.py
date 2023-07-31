import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

st.set_page_config("Streamlit YouTubers", "📺", layout="wide")
st.title("📺 Streamlit YouTubers")

st.warning("Streamlit YouTubers is a list of YouTube channels creating content on the use of Streamlit to build data apps.")

# Read in data from the Google Sheets
# Uses st.cache_data to only rerun when the query changes or after 10 min.
#@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gsheets_url"])

# Get number of videos in YouTube playlist
def get_num_videos(playlist_url):
    response = requests.get(playlist_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return len(soup.find_all('ytd-playlist-video-renderer'))

url = 'https://www.youtube.com/playlist?list=PLpdmBGJ6ELUI6Tws8BqVVNadsYOQlWGtw'
st.write(get_number_of_videos(url))

column_configuration = {
    "name": st.column_config.TextColumn(
        "Name", help="Name of YouTube channels", max_chars=100
    ),
    "youtube_id": st.column_config.TextColumn(
        "YouTube Channel ID", help="ID of YouTube channels", max_chars=100
    ),
    "avatar": st.column_config.ImageColumn("Avatar", help="YouTube channel's avatar"),
    "streamlit_playlist": st.column_config.LinkColumn(
        "Streamlit Playlist", help="Playlist of Streamlit tutorial videos", max_chars=100
    )
}

st.dataframe(df, column_config=column_configuration, use_container_width=True, hide_index=True,)
