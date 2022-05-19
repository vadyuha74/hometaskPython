# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
from random import randint

numblist = []
for i in range(20):
    numblist.append(randint(1, 10)) # задаем последовательность из 20 элементов рандомно
print(numblist)
newnumblist = []
for i in numblist:
    if numblist.count(i) == 1:
        newnumblist.append(i)
print(newnumblist)
        
