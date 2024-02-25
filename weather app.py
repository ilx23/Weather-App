from tkinter import *
from tkinter import messagebox
import requests


def get_weather(city):
    """
    Function to fetch weather data for the given city from WeatherAPI.
    """
    api_key = '8e4d57ff2ddb42e3862204101242002'  # Your WeatherAPI API key
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'

    try:
        # Sending a GET request to WeatherAPI
        response = requests.get(url)

        # Parsing the JSON response
        weather_data = response.json()

        if 'error' not in weather_data:
            # Extracting weather information from the API response
            weather_description = weather_data['current']['condition']['text']
            temperature = weather_data['current']['temp_c']
            humidity = weather_data['current']['humidity']
            wind_speed = weather_data['current']['wind_kph']

            # Updating the weather result label with the fetched data
            weather_result_label.config(
                text=f"Weather: {weather_description}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed:"
                     f" {wind_speed} km/h")
        else:
            # Displaying an error message if the city is not found
            messagebox.showerror("Error", "City Not Found! TRY AGAIN")
    except requests.RequestException as e:
        # Displaying an error message if the request to WeatherAPI fails
        messagebox.showerror("Error", f"Failed to retrieve weather data: {e}")


def search():
    """
    Function to handle the search button click event.
    """
    city = city_entry.get()  # Get the city name entered by the user
    city_entry.delete(0, END)  # Clear the city entry field after searching
    get_weather(city)  # Fetch and display weather information for the entered city


# GUI setup
app = Tk()
app.title("Weather App")
app.geometry("300x300")

# Title label for the Weather App
weather_app_title = Label(app, text="Weather App", font=("Helvetica", 15))
weather_app_title.pack(pady=10)

# Frame to hold the city entry field and search button
app_frame = Frame(app)
app_frame.pack(pady=20)

# Entry field for users to enter the city name
city_entry = Entry(app_frame, font=('Arial', 14), relief=GROOVE, borderwidth=1)
city_entry.pack()

# Search button to trigger weather search
search_button = Button(app_frame, text="Search", relief=GROOVE, borderwidth=2, font=('Arial', 12), command=search)
search_button.pack(pady=10)

# Label to display weather result
weather_result_label = Label(app, font=('Arial', 14), justify='left')
weather_result_label.pack(pady=20)

app.mainloop()
