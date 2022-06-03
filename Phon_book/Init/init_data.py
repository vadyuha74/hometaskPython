import os

list_kont = []
def InitKontakts():
    global list_kont
    path = os.getcwd()
    if os.path.exists(os.path.join(path, 'Kontakts.txt')):
        file = open(os.path.join(path, 'Kontakts.txt'), 'r')
        list_kont =[currelt_list.rstrip() for currelt_list in file.readlines()]
        file.close()
    return list_kont

