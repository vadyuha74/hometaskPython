import math

def CheckDig():
    n = input('Введите натуральное число ')
    while n.isdigit() == False or int(n) < 1:
        n = input('Нужно ввести натуральное число: ')
    return int(n)

def PrimFactos(n):
    # i = 2
    # result = []
    # while n > 1:
    #     if n % i == 0:
    #         result.append(i)
    #         n /= i
    #     else:
    #         i += 1
    result = [i for i in range(2, int(math.sqrt(n))+1) if not n % i]
    return result

n = CheckDig()
print(PrimFactos(n))