# Вычислить число Пи c заданной точностью d
# from cmath import pi
# a = int(input('Задайте точность числа π: '))
# print(round(pi, a))    
import requests
s_city = "Samara,RU"
city_id = 0
appid = "буквенно-цифровой APPID"
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                 params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': 'd6843ab8ee963f5d372296dfff62aed7'})
    data = res.json()
    cities = ["{} ({})".format(d['name'], d['sys']['country'])
              for d in data['list']]
    print("city:", cities)
    city_id = data['list'][0]['id']
    print('city_id=', city_id)
except Exception as e:
    print("Exception (find):", e)
    pass
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': '499068', 'units': 'metric', 'lang': 'ru', 'APPID': 'd6843ab8ee963f5d372296dfff62aed7'})
    data = res.json()
    print("conditions:", data['weather'][0]['description'])
    print("temp:", data['main']['temp'])
    print("temp_min:", data['main']['temp_min'])
    print("temp_max:", data['main']['temp_max'])
except Exception as e:
    print("Exception (weather):", e)
    pass