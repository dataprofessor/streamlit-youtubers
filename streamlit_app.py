import streamlit as st
import pandas as pd

# Read in data from the Google Sheets
# Uses st.cache_data to only rerun when the query changes or after 10 min.
#@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gsheets_url"])

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
