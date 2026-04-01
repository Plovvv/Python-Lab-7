import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

#1 OpenWeatherMap
city_name = 'Moscow'
KEY = os.getenv("API_KEY_weather")

def getCoordinates():
    try:
        response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},&limit=1&appid={KEY}')
        result = json.loads(response.text.strip('[').strip(']'))
        lat = result['lat']
        lon = result['lon']
        getWeather(lat, lon)
    except:
        print('Город с таким названием не был найден.')



def getWeather(lat, lon):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={KEY}&units=metric&lang=ru')
    result = json.loads(response.text)
    weather = result['weather'][0]['description']
    temp = result['main']['temp']
    humidity = result['main']['humidity']
    pressure = result['main']['pressure']
    print(f'Погода в городе {result['name']}: {weather}\nтемпература: {temp}°C\nвлажность: {humidity}%\nдавление: {pressure}hPa')



if __name__ == '__main__':
    getCoordinates()



#2 - News API
KEY = os.getenv("API_KEY_news")

def getNews(theme):
    response = requests.get(f'https://newsapi.org/v2/everything?q={theme}&language=ru&pageSize=1&apiKey={KEY}')
    result = json.loads(response.text)
    source = result['articles'][0]['source']['name']
    author = result['articles'][0]['author']
    title = result['articles'][0]['title']
    data = result['articles'][0]['publishedAt']

    print(f'Самая новая статья на тему "{theme}": "{title}", от {author}, с {source}, от {data}')

getNews('lada')