# Вычислить число Пи c заданной точностью d
from cmath import pi


a = int(input('Задайте точность числа π: '))
print(round(pi, a))    