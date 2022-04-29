# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

while True:
    n = input('Введите натуральное число: ')
    try:
        n = int(n)
        if n > 0:
            break
        else:
            print('Вы ввели неправильно')
    except ValueError:
        print('Вы ввели неправильно')
list = []
for i in range(1, n + 1):
    if n % i == 0:
        list.append(i)
print(list)
