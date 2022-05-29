# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
from random import randint


def InputNum(): # проверка ввода числа
    n = input('Введите количество забираемых конфет ')
    while n.isdigit() == False or int(n) > 28 or int(n) < 1:
        n = input('Нужно ввести только число от 1 до 28: ')
    return int(n)

def GamePlayer2(count): # игра вдвоем
    gamer1, gamer2 = input('Введите имя игрока 1: '), input(
        'Введите имя игрока 2: ')
    if randint(0, 1) == 0:
        currentgamer = gamer1
        print(f'Право первого хода выпало у {gamer2}')
    else:
        currentgamer = gamer2
        print(f'Право первого хода выпало у {gamer1}')
    while count>0:
        currentgamer = gamer2 if currentgamer == gamer1 else gamer1
        print(f'Ходит игрок {currentgamer}, осталось {count} конфет')
        k = InputNum()
        count -= k
    print('Победил ', currentgamer)

def GamePlayer1(count): # игра с компьютером
    gamer = input('Введите ваше имя ')
    if randint(0, 1) == 0:
        print(f'Право первого хода выпало у {gamer}')
        while True:
            print(f'Ходит игрок {gamer}, осталось {count} конфет')
            k = InputNum()
            count -= k
            if count < 1:
                print('Вы выиграли')
                break
            print(f'Моя очередь, осталось {count} конфет')
            k = count % 29 if ((count // 29)%2 == 1 and (count % 29) != 0)else 29 - k
            print(f'я забираю {k}')
            count -= k
            if count < 1:
                print('Я выиграл')
                break
    else:
        print(f'Право первого хода выпало у меня')
        while True:
            k = count % 29 if ((count // 29)%2 == 1 and (count % 29) != 0)else 29 - k
            print(f'я забираю {k}')
            count -= k
            if count < 1:
                print('Я выиграл')
                break
            print(f'Ходит игрок {gamer}, осталось {count} конфет')
            k = InputNum()
            count -= k
            if count < 1:
                print('Вы выиграли')
                break


print("На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. \n"
      "Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.")
while True:
    print('1 - Игра вдвоем\n2 - Играть одному\n3 - Выйти из игры\n')
    k = input('Если выбрали, введите номер ')
    while k.isdigit() == False or int(k) > 3 or int(k) < 1:
        k = input('Нужно ввести только число от 1 до 3: ')
    if int(k) == 1:
        GamePlayer2(2021)
    elif int(k) == 2:
        GamePlayer1(2021)
    elif int(k) == 3:
        print('Всего хорошего!!!')
        break
    else:
         continue
