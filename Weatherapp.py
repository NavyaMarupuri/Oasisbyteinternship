import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # You can adjust the unit (metric, imperial, standard)
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error: {response.status_code}")
        return None

def display_weather(weather_data):
    if weather_data:
        print(f"Weather in {weather_data['name']}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Conditions: {weather_data['weather'][0]['description']}")
    else:
        print("Unable to retrieve weather data.")

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    location = input("Enter city name: ")
    
    weather_data = get_weather(api_key, location)
    display_weather(weather_data)
