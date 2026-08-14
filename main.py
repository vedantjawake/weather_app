import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Weather App",
    page_icon="🌤️",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#74ebd5,#ACB6E5);
}

.main-title{
    font-size:50px;
    text-align:center;
    color:white;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:white;
    font-size:20px;
    margin-bottom:30px;
}

# .weather-card{
#     background:white;
#     padding:25px;
#     border-radius:20px;
#     box-shadow:0px 8px 25px rgba(0,0,0,0.2);
# }

.metric-box{
    background:#F4F6F7;
    padding:15px;
    border-radius:15px;
    text-align:center;
    margin:5px;
}

.footer{
    text-align:center;
    color:white;
    margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<h1 class='main-title'>🌤 Weather Dashboard</h1>", unsafe_allow_html=True)

st.markdown("<p class='subtitle'>Get real-time weather information for any city.</p>", unsafe_allow_html=True)

# ---------------- API KEY ----------------
API_KEY = os.getenv("MY_WEATHER_API")

# ---------------- INPUT ----------------
city = st.text_input(
    "🔍 Enter City Name",
    placeholder="Example: Mumbai"
)

search = st.button("🌦 Get Weather")

# ---------------- WEATHER ----------------
if search:

    if city == "":
        st.warning("Please enter a city name.")

    else:

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            city_name = data["name"]
            country = data["sys"]["country"]

            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]

            wind_speed = data["wind"]["speed"]

            weather = data["weather"][0]["main"]
            description = data["weather"][0]["description"]

            icon = data["weather"][0]["icon"]

            icon_url = f"https://openweathermap.org/img/wn/{icon}@4x.png"

            st.markdown("<div class='weather-card'>", unsafe_allow_html=True)

            col1, col2 = st.columns([1,2])

            with col1:
                st.image(icon_url, width=180)

            with col2:

                st.markdown(f"## 📍 {city_name}, {country}")

                st.markdown(f"### 🌥 {weather}")

                st.write(description.title())

                st.markdown(f"# 🌡 {temperature} °C")

                st.write(f"Feels Like : **{feels_like} °C**")

            st.markdown("---")

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric("💧 Humidity", f"{humidity}%")

            with c2:
                st.metric("🌬 Wind Speed", f"{wind_speed} m/s")

            with c3:
                st.metric("⚡ Pressure", f"{pressure} hPa")

            st.markdown("</div>", unsafe_allow_html=True)

        else:

            st.error(response.json().get("message", "Unknown Error"))

# ---------------- FOOTER ----------------
st.markdown("""
<div class='footer'>
Made with ❤️ using Streamlit
</div>
""", unsafe_allow_html=True)            