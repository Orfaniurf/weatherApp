import flet as ft
from main import get_weather
import os

def main(page: ft.Page):

    page.title = "Weather App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    t = ft.Text(value='Weather App', color='blue', size=35, weight='bold')
    txt = ft.TextField(label='Insert City (ex. New York)', width=250, border_radius=20, text_align=ft.TextAlign.CENTER)
    weather_icon = ft.Icon(name='wb_sunny', size=80, color='yellow')

    t_result = ft.Text(value='', size=20)

    def submit(e):
        if not txt.value:
            txt.error_text = 'Please enter a city name'
            page.update()
        else:
            txt.error_text = None
            city = txt.value
            data = get_weather(city)

            if data is None:
                t_result.value = "City doesn't found or connection error"
                t_result.color = 'red'
            else:
                city_name = data['name']
                temp = data['main']['temp']
                desc = data['weather'][0]['description']
                hum = data['main']['humidity']

                t_result.value = f"{city_name}\nTemperature: {temp:.1f}°C\n{desc.capitalize()}\nHumidity: {hum}%"
                t_result.color = "white"

                desc_lower = desc.lower()

                if "cloud" in desc_lower:
                    weather_icon.name = "cloud"
                    weather_icon.color = "grey"
                elif "rain" in desc_lower or "drizzle" in desc_lower:
                    weather_icon.name = "water_drop"
                    weather_icon.color = "blue"
                elif "snow" in desc_lower:
                    weather_icon.name = "ac_unit"
                    weather_icon.color = "cyan"
                elif "storm" in desc_lower or "thunder" in desc_lower:
                    weather_icon.name = "thunderstorm"
                    weather_icon.color = "purple"
                elif "clear" in desc_lower or "sun" in desc_lower:
                    weather_icon.name = "wb_sunny"
                    weather_icon.color = "yellow"
                elif "fog" in desc_lower or "mist" in desc_lower:
                    weather_icon.name = "blur_on"
                    weather_icon.color = "grey"
                else:
                    weather_icon.name = "wb_cloudy_outlined"
                    weather_icon.color = "white"
            page.update()
    
    
    btn = ft.ElevatedButton('Search', icon='search', on_click=submit, bgcolor='blue', color='white')
    txt.on_submit = submit
    

    page.add(
        t,
        ft.Divider(height=20, color='transparent'),
        weather_icon,
        ft.Divider(height=20, color='transparent'),
        ft.Row([txt,btn],alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(height=20, color='transparent'),
        t_result
    )

os.environ["LIBGL_ALWAYS_SOFTWARE"] = "1"
ft.app(target=main)