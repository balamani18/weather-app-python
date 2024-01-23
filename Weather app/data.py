import requests

city_name = 'chennai'
API_key = '52330cb6892813208901c168238eb6fe'
url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units-metric'

response = requests.get(url)
if response.status_code ==200:
    data= response.json()
    print('weather temperature is ',data ["weather"][0]["description"])
    print('current temperature is' ,data['main']['temp'])
    print('current temperature feels likes is', data['main']['feels_like']) 
    