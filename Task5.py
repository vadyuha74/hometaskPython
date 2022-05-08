# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов (нет нулевых кофициентов).

def PolinToList(Polstr):
    Polstr = Polstr[:-2]
    symbols = ['x', '\u2070', '\u00B9', '\u00B2', '\u00B3', '\u2074', '\u2075', '\u2076', '\u2077', '\u2078', '\u2079']
    for chr in symbols:
        if chr in Polstr:
            Polstr = Polstr.replace(chr,'')
    coeflist = [int(x) for x in Polstr.split('+') if x.isdigit()]
    return coeflist

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

data = open('a.txt', 'r')
firstpolin = data.read()
data.close()
list1 = PolinToList(firstpolin)
data = open('b.txt', 'r')
secondpolin = data.read()
data.close()
list2 = PolinToList(secondpolin)
if len(list1) > len(list2):
    list2.extend([0,] * (len(list1) - len(list2)))
else: 
    list1.extend([0,] * (len(list2) - len(list1)))
summ = map(sum, zip(list1, list2))
result = CreatPolnum(list(summ))
print("полученый многочлен:",result)
fl = input('Задайте имя файла для сохранения: ')
#fl += '.txt'
data = open(fl+'.txt', 'w')
data.writelines(result)
data.close()