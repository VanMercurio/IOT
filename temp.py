import requests

url = "https://weather-api99.p.rapidapi.com/weather"

querystring = {"city": "campinas"}

headers = {
    "X-RapidAPI-Key": "e4ec702a75msh06cb430c8f487abp16119ajsnc005c091e8f0",
    "X-RapidAPI-Host": "weather-api99.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
