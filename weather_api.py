import requests

def get_weather(city, api_key="your_openweathermap_api_key"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200:
        raise Exception(data.get("message", "API error"))
    return {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "weather": data["weather"][0]["main"]
    }
