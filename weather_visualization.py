import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Constants
API_KEY = "b157f3ac6ed1e304a6f3624e3ca2b878"  # Your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"
CITY = "Tokyo"  # City name for weather forecast

def fetch_weather_data(city, api_key):
    """
    Fetch weather data from OpenWeatherMap 5 Day / 3 Hour Forecast API.
    :param city: City name
    :param api_key: API key for OpenWeatherMap
    :return: Parsed JSON response
    """
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data:", response.status_code, response.text)
        return None

def process_weather_data(data):
    """
    Process the weather data into a DataFrame.
    :param data: Raw JSON response from API
    :return: Processed pandas DataFrame
    """
    weather_list = data["list"]
    processed_data = {
        "DateTime": [pd.to_datetime(entry["dt"], unit="s") for entry in weather_list],
        "Temperature (°C)": [entry["main"]["temp"] for entry in weather_list],
        "Humidity (%)": [entry["main"]["humidity"] for entry in weather_list],
        "Wind Speed (m/s)": [entry["wind"]["speed"] for entry in weather_list],
    }
    return pd.DataFrame(processed_data)

def create_visualizations(df):
    """
    Create visualizations for the weather data.
    :param df: pandas DataFrame containing weather data
    """
    plt.figure(figsize=(12, 6))
    
    # Line plot for temperature over time
    sns.lineplot(data=df, x="DateTime", y="Temperature (°C)", label="Temperature (°C)", marker="o", color="blue")
    plt.title("Temperature Forecast")
    plt.xlabel("Date and Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Line plot for humidity
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x="DateTime", y="Humidity (%)", label="Humidity (%)", marker="o", color="skyblue")
    plt.title("Humidity Forecast")
    plt.xlabel("Date and Time")
    plt.ylabel("Humidity (%)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Line plot for wind speed
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x="DateTime", y="Wind Speed (m/s)", label="Wind Speed (m/s)", marker="o", color="green")
    plt.title("Wind Speed Forecast")
    plt.xlabel("Date and Time")
    plt.ylabel("Wind Speed (m/s)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to fetch, process, and visualize weather data.
    """
    print("Fetching weather data...")
    weather_data = fetch_weather_data(CITY, API_KEY)
    if weather_data:
        print("Processing weather data...")
        df = process_weather_data(weather_data)
        print("Visualizing weather data...")
        create_visualizations(df)
    else:
        print("Could not fetch weather data. Please check the API key or parameters.")

if __name__ == "__main__":
    main()
