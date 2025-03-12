import streamlit as st

def profile():
    st.title("My Profile")

    with st.form(key="profile_form"):
        name = st.text_input("Full Name", "")
        email = st.text_input("Email", "")
        bio = st.text_area("Short Bio", "")

        submit = st.form_submit_button("Save Changes")

    if submit:
        st.success("Profile updated successfully!")

if __name__ == "__main__":
    profile()
