import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(city):
    api_key = 'a67ab0424e6e180d335be1f3634bd1aa'  # Replace 'YOUR_API_KEY' with your actual API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # You can change units to imperial for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        return None

def display_weather():
    city = entry_city.get()
    # Encode city to UTF-8 for non-English characters
    city_encoded = city.encode('utf-8')

    weather_data = get_weather(city_encoded.decode())

    if weather_data:
        temperature = f"Temperature: {weather_data['main']['temp']}°C"
        humidity = f"Humidity: {weather_data['main']['humidity']}%"
        wind_speed = f"Wind Speed: {weather_data['wind']['speed']} m/s"
        description = f"Description: {weather_data['weather'][0]['description']}"

        result_label.config(text=f"Weather in {city}\n{temperature}\n{humidity}\n{wind_speed}\n{description}")
    else:
        messagebox.showerror("Error", "Failed to fetch weather data for the provided city.")

root = tk.Tk()
root.title("Weather Forecast")

label_city = tk.Label(root, text="Enter city name:")
label_city.pack()

entry_city = tk.Entry(root)
entry_city.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=display_weather)
get_weather_button.pack()

result_label = tk.Label(root, text="", wraplength=300)
result_label.pack()

root.mainloop()
