from tkinter import*
from tkinter import messagebox
import Init
import csv


def delete():
    select = listbox.curselection()
    listbox.delete(select[0], select[-1])

def add():
    name = entry1.get()
    telephone = entry2.get()
    if name == "":
        messagebox.showerror('Warning', 'Нет имени')
    elif telephone == "":
        messagebox.showerror('Warning', 'Не указан телефон')
    else:
        listbox.insert(0, name + ' : ' + telephone)
        entry1.delete(0, END)
        entry2.delete(0, END)


def save():
    list1 = list(listbox.get(0, END))
    with open("Kontakts.txt", "w") as file:
        file.writelines("%s\n" % place for place in list1)
    res = messagebox.askyesno('Можем сохранить и в csv файле', 'Сохранить csv файле')
    if res:
        with open("Kontakts.csv", mode="w", encoding='utf-8') as file:
            names = ["Имя", "Телефон"]
            file_writer = csv.writer(file, delimiter=",", lineterminator="\r")
            file_writer.writerow(names)
            for kont in list1:
                names = kont.split(' : ')
                file_writer.writerow(names)


win = Tk()
win.geometry("500x400+550+300")
win.title("Контакты телефонов")

frame1 = Frame(win)
frame2 = Frame(win)
frame1.pack()
frame2.pack()

label1 = Label(frame1, text="Список контактов", font="Calibre 30")
label1.grid(row=0, columnspan=2)
label2 = Label(frame1, text="Имя:", font="Calibre 18")
label2.grid(row=1, column=0)
label3 = Label(frame1, text="Телефон:", font="Calibre 18")
label3.grid(row=2, column=0)

name = StringVar()
entry1 = Entry(frame1, textvariable=name)
entry1.grid(row=1, column=1)

telephone = StringVar()
entry2 = Entry(frame1, textvariable=telephone)
entry2.grid(row=2, column=1)

scrollbar = Scrollbar(frame2, orient=VERTICAL)
listbox = Listbox(frame2, selectmode=EXTENDED,
                  yscrollcommand=scrollbar.set, width=40)
listbox.grid(row=3, columnspan=3)
scrollbar.config(command=listbox)
for i in Init.InitKontakts():
    listbox.insert(0, i)

button1 = Button(frame2, text="Добавить", width=15, height=1, command=add)
button1.grid(row=5, column=0)
button2 = Button(frame2, text="Удалить",  width=15, height=1, command=delete)
button2.grid(row=5, column=1)
button3 = Button(frame2, text="Сохранить в файл",
                 width=15, height=1, command=save)
button3.grid(row=5, column=2)

win.mainloop()
