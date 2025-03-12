import streamlit as st

def home():
    st.title("Welcome to CriolloList 🎉")
    st.write("A student-driven marketplace for services at your university!")

    st.image("assets/logo.jpg", use_container_width=True)

    st.subheader("Why use CriolloList?")
    st.markdown("""
    - 🏫 **Campus-Focused**: Find services offered by students in your university.
    - 🚀 **Boost Visibility**: Promote your skills and small business.
    - 🔍 **Easy Search & Categories**: Find exactly what you need in a few clicks.
    """)

    if st.button("Browse Listings"):
        st.switch_page("pages/listings.py")

if __name__ == "__main__":
    home()
