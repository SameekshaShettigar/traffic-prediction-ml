import streamlit as st
import pickle

# Load model and city mapping
model = pickle.load(open("model.pkl", "rb"))
city_mapping = pickle.load(open("city_map.pkl", "rb"))

# Reverse mapping
city_map_rev = {v: k for k, v in city_mapping.items()}

# UI Styling
st.set_page_config(page_title="Traffic Predictor", page_icon="🚦", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #FF4B4B;'>🚦 Traffic Prediction System</h1>
    <p style='text-align: center;'>Predict traffic based on city and time</p>
""", unsafe_allow_html=True)

# Select City
city = st.selectbox("🌆 Select City", list(city_map_rev.keys()))

# Time selector (AM/PM)
col1, col2 = st.columns(2)

with col1:
    hour = st.selectbox("🕒 Hour", list(range(1, 13)))

with col2:
    period = st.selectbox("⏳ AM / PM", ["AM", "PM"])

# Convert to 24-hour format
if period == "PM" and hour != 12:
    hour_24 = hour + 12
elif period == "AM" and hour == 12:
    hour_24 = 0
else:
    hour_24 = hour

# Predict
if st.button("🚀 Predict Traffic"):
    city_code = city_map_rev[city]
    pred = model.predict([[city_code, hour_24]])[0]

    # Traffic level
    if pred < 30:
        level = "🟢 LOW"
    elif pred < 70:
        level = "🟡 MEDIUM"
    else:
        level = "🔴 HIGH"

    st.markdown("---")
    st.subheader(f"📊 Traffic Level: {level}")
    st.write(f"🚗 Estimated Vehicles: {pred:.2f}")