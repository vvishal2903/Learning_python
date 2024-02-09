import requests

def get_weather(api_key,city):
    base_url = "https://api.openweathermap.org/data/3.0/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url,params=params)
    


api_key = "e37516164d434e993b9122713f2bd8b9"
city = input("Enter your city: ")
