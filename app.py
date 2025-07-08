import streamlit as st
import pandas as pd
import json

# Load mock data
with open("mock_hotel_data.json", "r") as file:
    hotel_data = json.load(file)

df = pd.DataFrame(hotel_data)

st.set_page_config(page_title="Hotel Listings", layout="wide")
st.title("🏨 Hotel Listings - Booking.com Style Prototype")

# City filter
cities = df['city'].unique()
selected_city = st.selectbox("Filter by City", cities)

filtered_hotels = df[df['city'] == selected_city]

st.markdown("---")

for index, row in filtered_hotels.iterrows():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(row["image"], width=250)
    with col2:
        st.subheader(row["name"])
        st.write(f"📍 **City:** {row['city']}")
        st.write(f"⭐ **Rating:** {row['rating']}")
        st.write(f"💰 **Price per Night:** ₹{row['price_per_night']}")
        st.write("✅ Available" if row['available'] else "❌ Not Available")
        st.button("Book Now", key=row["name"] + "_btn")

    st.markdown("---")
