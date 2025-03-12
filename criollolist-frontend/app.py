import streamlit as st
from pages import home, listings, profile, about  # Import the separate page modules

# Set the page title and layout
st.set_page_config(page_title="CriolloList", page_icon="📝", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Listings", "Profile", "About"], index=0)

# Redirect to the correct page
if page == "Home":
    home.home()  # Redirect to home.py
elif page == "Listings":
    listings.listings()  # Redirect to listings.py
elif page == "Profile":
    profile.profile()  # Redirect to profile.py
elif page == "About":
    about.about()  # Redirect to about.py
