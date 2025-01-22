# Import required libraries
import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Function to fetch data from OpenWeatherMap API
def fetch_weather_data(city, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

# Function to extract relevant data
def extract_weather_metrics(data):
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    return temp, humidity, pressure

# Function to visualize data
def visualize_weather_metrics(temp, humidity, pressure):
    metrics = ['Temperature', 'Humidity', 'Pressure']
    values = [temp, humidity, pressure]

    sns.barplot(x=metrics, y=values)
    plt.title('Weather Metrics')
    plt.show()

# Main execution
if __name__ == "__main__":
    api_key = '48edc8f05b7461754d7e6bcd0a05cdcc'  # Replace with your actual API key
    city = 'Hyderabad'  # You can change this to any city you like

    # Fetch data from API
    weather_data = fetch_weather_data(city, api_key)

    # Extract relevant metrics
    temp, humidity, pressure = extract_weather_metrics(weather_data)

    # Visualize the extracted data
    visualize_weather_metrics(temp, humidity, pressure)
