# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def InCheckDig():
    n = input('Введите натуральное число больше 1 ')
    while n.isdigit() == False or int(n) < 2:
        n = input('Нужно ввести натуральное число больше 1: ')
    return int(n)

def PrimFactos(n):
    i = 2
    while n > 1:
        if n % i:
            i += 1
        else:
            yield i
            n /= i
print('раскладываем чилсо на простые множители')
n = InCheckDig()
print(f'{n} = {" * ".join(map(str, PrimFactos(n)))}')