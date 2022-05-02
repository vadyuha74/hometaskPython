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

def CreatDegree(deg):
    degree = {"0": "\u2070",
           "1": "\u00B9",
           "2": "\u00B2",
           "3": "\u00B3",
           "4": "\u2074",
           "5": "\u2075",
           "6": "\u2076",
           "7": "\u2077",
           "8": "\u2078",
           "9": "\u2079",
           }
    temp = ""
    char = str(deg)
    if deg == 1:
        return "x"
    else:
        for i in char:
            temp += degree[i]
        return 'x'+temp

def RandList(l:int):
    list = []
    for i in range(l):
        list.append(randint(1, 100))
    return list

print('задаем степень многочлена')
k = InputNum()
memb = RandList(k+1)
polnum = ""
i = 0
while k > 0:
    if memb[i] != 0:
        polnum += str(memb[i]) + CreatDegree(k) + '+'
    i += 1
    k -= 1
else:
    polnum += str(memb[-1]) + '=0'
print(f"полученый многочлен:",polnum)
data = open('file.txt', 'w')
data.writelines(polnum)
data.close()