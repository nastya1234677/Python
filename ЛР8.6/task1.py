import requests

url = 'https://wttr.in'

weather_parameters = {
 'T': '0',
}

response = requests.get(url, params=weather_parameters)

print(response.text)
