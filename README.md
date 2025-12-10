# 🌦️ Weather Fetcher Pro

A modern desktop application to check real-time weather conditions, built with **Python** and **Flet**.

![Status](https://img.shields.io/badge/Status-Active-green)
![Python](https://img.shields.io/badge/Python-3.10+-blue)

## 🚀 Features
- **Global Search:** Check weather for any city (New York, Tokyo...).
- **Modern UI:** Clean interface built with Flet (Material Design).
- **Dynamic Icons:** Visual feedback changes based on weather (Sunny, Rainy, Cloudy).

## 🛠️ Tech Stack
- **Frontend:** Flet (Python GUI)
- **Backend:** Python (`main.py`)
- **API:** OpenWeatherMap
- **Security:** Python-dotenv (for API Key management)

## 📦 How to Use
1. **Clone the repository**
   Open your terminal and run this command: 
   ```git clone https://github.com/Orfaniurf/weatherApp.git```
   ```cd weatherApp```

**2. Set up the password**
   Create a file named `.env` inside the folder and write this line inside it: ```OPENWEATHER_API_KEY=your_key_here```

**3. Install libraries**
   Go back to the terminal and run: ```pip install -r requirements.txt```

   > **⚠️ Linux Users:** If the app crashes, install the media libraries:
   > ```sudo apt install libmpv1 libgtk-3-0```

**4. Start the App**
   To open the window, run this final command: ```python app_gui.py```