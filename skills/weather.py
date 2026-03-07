import requests

API_KEY = "YOUR_API_KEY"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code != 200:
        return "Weather service failed."

    data = response.json()

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    return f"The weather in {city} is {desc} with temperature {temp}°C."