import os

list_kont = []
def Init_base():
    global list_kont
    path = os.getcwd()
    print(path)
    if os.path.exists(os.path.join(path, 'Database/Сотрудники.txt')):
        file = open(os.path.join(path, 'Database/Сотрудники.txt'), 'r')
        list_kont =[currelt_list.rstrip() for currelt_list in file.readlines()]
        file.close()
    return list_kont
