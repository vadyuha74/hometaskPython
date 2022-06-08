from telegram import Update
from telegram.ext import CallbackContext
from logging import log
import datetime
import requests
EXtext = ''
startEX = 0


def get_value(f = False, RUB = 1):
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    date_vlue = data['Valute']
    EXtext = ''
    Curse = ['KGS', 'KZT', 'USD', 'EUR', 'TRY', 'CNY']

    if RUB > 0:
        for i in date_vlue.items():
            # print(i[1]['Name'], i[1]['Nominal'] / i[1]['Value'])
            # print(float('{0:.3f}'.format(i[1]['Nominal'] / i[1]['Value'])))
            if i[0] == Curse[0] or i[0] == Curse[1] or i[0] == Curse[2] or i[0] == Curse[3] or i[0] == Curse[4] or i[
                0] == Curse[5]:
                EXtext += f"{RUB} - RUB == {float('{0:.3f}'.format(RUB * (i[1]['Nominal'] / i[1]['Value'])))} - {i[0]} \n"
    return EXtext

def getNumber(msg):
    number = msg.split(" ")
    if len(number) == 1:
        return -1
    for i in number:
        if i.isdigit():
            return int(i)
    return -1

def Calc_Exchange(update: Update, context: CallbackContext) -> None:
    log(update, context)
    number = getNumber(update.message.text)
    text = ''
    print(text)
    if number != -1:
        result = get_value(RUB=number)
    else:
        update.message.reply_text(f'Что то пошло не так '
                                  f'\nПопробуйте ввести /Calc_Exchange и через пробел количество рублей! иначе ответа от меня не дождетесь ха-ха-ха '
                                  f'\nПример: '
                                  f'\n/Calc_Exchange 500')

    update.message.reply_text(result)


def Exchange(update: Update, context: CallbackContext) -> None:
    log(update, context)
    msg = update.message.text
    text = ''
    print(text)
    try:
        result = get_value()
    except:
        update.message.reply_text(f'Что то пошло не так попробуйте ввести все числа и символы через пробел!')

    update.message.reply_text(result)


def hi(update: Update, context: CallbackContext) -> None:
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}')


def help(update: Update, context: CallbackContext) -> None:
    log(update, context)
    update.message.reply_text(f'/hi - Приветсвие '
                              f'\n/sum a b '
                              f'\n/math Введите математическое выражение все числа и символы через пробел иначе ответа от меня не дождетесь ха-ха '
                              f'\nПример: /math 2 + 2 + 4 - 5 * 5 '
                              f'\n/time - время '
                              f'\n/help - список команд'
                              f'\n/Exchange - Возврашает курс валют'
                              f'\n/Calc_Exchange (количество рублей) - Введите количество рублей которые хотите конвертировать через пробел иначе ответа от меня не дождетесь ха-ха-ха'
                              ) #f'\n/getVideo - Возврашает видео')


def time(update: Update, context: CallbackContext) -> None:
    log(update, context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')


def sum(update: Update, context: CallbackContext) -> None:
    log(update, context)
    msg = update.message.text.split()
    a = int(msg[1])
    b = int(msg[2])

    update.message.reply_text(f'{a} + {b} = {a + b}')
def math(update: Update, context: CallbackContext) -> None:
    log(update, context)
    msg = update.message.text
    text = ''
    for i in msg.split():
        if i != '/math':
            text += i + ' '
    print(text)
    try:
        result = do(text)
    except:
        update.message.reply_text(f'Что то пошло не так попробуйте ввести все числа и символы через пробел!')

    update.message.reply_text(f'{text} = {result[0]}')