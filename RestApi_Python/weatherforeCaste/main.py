import requests

def get_weather(city, units='metric', api_key='f59149603f5c245d5d998625978e3a2e'):

#   url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}'
    r = requests.get(url)
    content = r.json()
    with open('data.txt', 'a') as file:
        for dicty in content['list']:
            # file.write(f"{dicty['dt_txt']}, {dicty['main']['temp']}, {dicty['weather'][0]['description']}\n")
            return file.write(f"{dicty['dt_txt']}, {dicty['main']['temp']}, {dicty['weather'][0]['description']}\n")
print(get_weather(city='Noida'))