import os

list_kont = []
def init_kontakts():
    global list_kont
    path = os.getcwd()
    print(path)
    try:
        file = open(os.path.join(path, 'Database/Сотрудники.txt'), 'r')
        list_kont = file.readlines()
        file.close()
        print(list_kont)
    except OSError:
        file = open(os.path.join(path, 'Database/Сотрудники.txt'), 'w')
        file.close()
    return list_kont
init_kontakts()