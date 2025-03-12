import streamlit as st

# Mock data for now
services = [
    {"name": "Graphic Design", "owner": "John Doe", "price": "$20/hr", "contact": "johndoe@email.com"},
    {"name": "Tutoring (Math)", "owner": "Alice Smith", "price": "$15/hr", "contact": "alice@email.com"},
    {"name": "3D Printing", "owner": "David Johnson", "price": "$10 per print", "contact": "david@email.com"},
]

def listings():
    st.title("Available Services")
    st.write("Find the best services offered by students!")

    # Search & filter (To be improved later)
    search_query = st.text_input("Search for a service", "")
    
    for service in services:
        if search_query.lower() in service["name"].lower():
            st.markdown(f"### {service['name']}")
            st.text(f"Offered by: {service['owner']}")
            st.text(f"Price: {service['price']}")
            st.text(f"Contact: {service['contact']}")
            st.write("---")

if __name__ == "__main__":
    listings()
