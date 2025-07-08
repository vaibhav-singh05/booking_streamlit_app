import streamlit as st
import pandas as pd
import json

# Load hotel data
with open("mock_hotel_data.json", "r") as file:
    hotel_data = json.load(file)

df = pd.DataFrame(hotel_data)

st.set_page_config(page_title="Hotel Listings", layout="wide")
st.title("🏨 Hotel Listings - Booking.com Style Prototype")

# Filter by city
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

    # 📝 About section
    st.markdown("### 📝 About this property")
    st.markdown(f"{row.get('description', 'No description available.')}")

    # 🛎️ Facilities section (3 columns)
    st.markdown("### 🛎️ Property Facilities")
    facilities = row.get("facilities", [])
    if facilities:
        col1, col2, col3 = st.columns(3)
        for i, fac in enumerate(facilities):
            if i % 3 == 0:
                col1.markdown(f"- {fac}")
            elif i % 3 == 1:
                col2.markdown(f"- {fac}")
            else:
                col3.markdown(f"- {fac}")
    else:
        st.write("No facilities listed.")

    # 🛏️ Room Packages
    st.markdown("### 🛏️ Room Packages")
    rooms = row.get("rooms", [])
    if rooms:
        for room in rooms:
            with st.expander(f"{room['type']} - ₹{room['price']}"):
                st.markdown(f"**Occupancy:** {room['occupancy']}")
                st.markdown(f"**Refund Policy:** {room['refund']}")
                st.markdown(f"**Meals:** {room['meal']}")
                st.button("Book this room", key=f"{row['name']}_{room['type']}")
    else:
        st.write("Room information is not available.")

    st.markdown("---")
