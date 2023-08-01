import requests

def get_weather_data(location, api_key):
    """
    Function to fetch weather data from OpenWeatherMap API based on location.
    Returns a dictionary containing weather information.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"appid": api_key, "units": "metric"}

    try:
        # Check if the user entered a valid zip code (numbers only)
        if location.isdigit():
            params["zip"] = location + ",us"
        else:
            params["q"] = location

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch weather data. Please check your input and try again.")
            return None

    except requests.exceptions.RequestException as e:
        print("Connection to the weather service failed. Please check your internet connection.")
        return None

def display_weather_forecast(weather_data):
    """
    Function to display weather forecast data in a readable format.
    """
    if weather_data is not None:
        city_name = weather_data["name"]
        weather_description = weather_data["weather"][0]["description"].capitalize()
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        print(f"Weather forecast for {city_name}:")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Weather data not available.")

def main():
    """
    Main function to run the weather application.
    """
    api_key = "8677a75924621747548ac844e7aecf1d"

    while True:
        user_input = input("Please enter a zip code or city name (type 'quit' to exit): ")

        if user_input.lower() == "quit":
            print("Exiting the weather application.")
            break

        # Validate if the user entered valid data (zip code or city name)
        if user_input.strip():
            weather_data = get_weather_data(user_input, api_key)
            display_weather_forecast(weather_data)
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()