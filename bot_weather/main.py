import telebot
from pyowm import OWM


def get_location(lat, lon):
    url = f"https://yandex.ru/pogoda/maps/nowcast?lat={lat}&lon={lon}&via=hnav&le_lightning=1"
    return url

def weather(city: str):
    owm = OWM('bed4363a34565fc32ca5bc2e78d2ed25')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    weather = observation.weather
    location = get_location(observation.location.lat, observation.location.lon)
    temperature = weather.temperature("celsius")
    return temperature, location
    
token = '5468425085:AAEXTChAQ-k3UC6cDYi7NJgae4pSn3IFr4s'
bot = telebot.Telebot(token)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/weather':
        bot.send_message(message.from_user.id, "Введите название города")
        bot.register_next_step_handler(message, get_weather)
    else:
        bot.send_message(message.from_user.id, 'Напиши /weather')


def get_weather(message):
    city = message.text
    try:
        w = weather(city)
        bot.send_message(message.from_user.id, f'В городе {city} сейчас {round(w[0]["temp"])} градусов,'
                                                 f'чувствуеться как {round(w[0]["feels_like"])} градусов')
        bot.send_message(message.from_user.id, w[1])
        bot.send_message(message.from_user.id, "Введите название города")
        bot.register_next_step_handler(message, get_weather)
    except Exception:
        bot.send_message(message.from_user.id, "Упс... Такого города нет в базе данных")
        bot.send_message(message.from_user.id, "Введите название города")
        bot.register_next_step_handler(message, get_weather)
bot.polling(non_stop=True, interval=0)