print('hello world')
# типы данных и переменная
# int, float, boolean. str, list, None
value = None
a = 123
b = 1.23
print(a)
print(b)
value = 1234
# указывает тип данных
# print(type(a))
# выод строки
s = 'hello "world"'
print(s)
# интерполяция вывод нескольких переменных способы
print(a, b, s)
print(a, '-', b, '-', s)
print('{} - {} - {}'.format(a, b, s))
print(f'{a} - {b} - {s}')
# массивов нет их заменяют списки
list = []
print(list)
list = [1, 2, 3]
col = ['1', '2', 3, 'hello']
print(list)
print(col)
# ввод и ввывод данных
# print() input()
# print('Введите d')
# d = input()
# print(d)
## по умолчанию вводяться строки пример ввод целых
# print('Введите c')
# c = int(input())
# print(c)
# арифмитические функции +,-,*,/,%- остаток от деления, //- целочисленное деление
# функция округления round()
g = 1.3
e = 3
f = g * e
print(f)
c = round(g * e, 3) # через запятую количество символов после запятой
print(c)
c += 3
print(c)
# логические операции
d = 1 < 4
print(d)
d = 1 < 4 and 5 < 6
print(d)
# логические операции в списках
mas = [1,3,4,5]
print(not 2 in mas) # нет 2 в списке?