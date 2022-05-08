# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#  (значения от 1 до 100, можно создать свой генератор случайных чисел или использовать готовый) многочлена 
#  и записать в файл многочлен степени k. Пример: k=2 => 2*x² + 4*x + 5
from random import randint


def InputNum():
    while True: # проверка ввода числа
        n = input('Введите натуральное число: ')
        try:
            n = int(n)
            if n > 0:
                break
            else:
                print('Вы ввели неправильно')
        except ValueError:
            print('Вы ввели неправильно')
    return n

def CreatPolnum(pol):
    degree = {"0": "\u2070",
            "1": "\u00B9",
            "2": "\u00B2",
            "3": "\u00B3",
            "4": "\u2074",
            "5": "\u2075",
            "6": "\u2076",
            "7": "\u2077",
            "8": "\u2078",
            "9": "\u2079",}
    polnum = ''
    k = len(pol)-1
    for i in range(len(pol)):
        if pol[i] == 0:
            polnum += ''
        elif k == 0:
            polnum += str(pol[i]) + '=0'
        elif k == 1:
            polnum += str(pol[i]) + 'x' + '+'
        elif pol[i] == 1:
            deg = ''
            for j in str(k):
                deg += degree[j]
            polnum += 'x' + deg + '+'
        else:
            deg = ''
            for j in str(k):
                deg += degree[j]
            polnum += str(pol[i]) + 'x' + deg + '+'
        k -= 1
    return polnum

def RandList(l:int):
    list = []
    for i in range(l):
        list.append(randint(1, 100))
    return list

print('задаем степень многочлена')
k = InputNum()
memb = RandList(k+1)
polnum = CreatPolnum(memb)
print("полученый многочлен:",polnum)
# fl = input('Задайте имя файла для сохранения: ')
# fl += '.txt'
# data = open(fl, 'w')
# data.writelines(polnum)
# data.close()