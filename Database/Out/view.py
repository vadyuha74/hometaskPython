from tkinter import*
from tkinter import messagebox
import Data 



def add(name, surname, pos):
    global list_kont
    if name == "":
        messagebox.showerror('Warning', 'Нет имени')
    elif surname == "":
        messagebox.showerror('Warning', 'Не фамилии')
    elif pos == "":
        messagebox.showerror('Warning', 'Не указана должность')
    else:
        list_kont.append({'имя': name, 'фамилия': surname, 'должность': pos})
        return f'{name} , {surname} , {pos}'

def save():
    global list_kont
    list1=list_kont 
    f=open('Database/Сотрудники.txt', "w")
    print("\n".join(map(str, list1)), file=f)
    f.close()
    res = messagebox.askyesno('Можем сохранить и в exel файле', 'Сохранить в exel файле')
    if res: 
        f=open('Database/Сотрудники.txt', "w")
        for i in list1:
            f.writelines(str(i+'\n'))
        f.close()

def Menu():
    global list_kont
    list_kont = Data.Init_base()
    win=Tk()
    win.geometry("+550+300")
    win.title("База данных")
    def get_entry(entry):
        s = entry.get()
        entry.delete(0, END)
        return s
    frame1=Frame(win)
    frame2=Frame(win)
    frame1.pack()
    frame2.pack()

    label1=Label(frame1, text="Список сотрудников", font="Calibre 30")
    label1.grid(row=0, columnspan=3)
    label2=Label(frame2, text="Имя", font="Calibre 18")
    label2.grid(row=0, column=0)
    label3=Label(frame2, text="Фамилия", font="Calibre 18")
    label3.grid(row=0, column=1)
    label4=Label(frame2, text="Должность", font="Calibre 18")
    label4.grid(row=0, column=2)

    name=StringVar()
    entry1=Entry(frame2,textvariable=name)
    entry1.grid(row=1, column=0)
    surname=StringVar()
    entry2=Entry(frame2,textvariable=surname)
    entry2.grid(row=1, column=1)
    pos=StringVar()
    entry3=Entry(frame2,textvariable=pos)
    entry3.grid(row=1, column=2)

    scrollbar=Scrollbar(frame1, orient=VERTICAL)
    listbox=Listbox(frame1, selectmode=SINGLE, yscrollcommand=scrollbar.set,width=50) 
    listbox.grid(row=3, columnspan=3)
    scrollbar.config(command=listbox)
    for i in list_kont:
        listbox.insert(0, i)
    button1=Button(frame2, text="Добавить", width=15, height=1, 
                command=lambda : listbox.insert(END, add(get_entry(entry1), get_entry(entry2), get_entry(entry3))))
    button1.grid(row=5, column=0)
    button2=Button(frame2, text="Удалить",  width=15, height=1, command=lambda : listbox.delete(listbox.curselection()))
    button2.grid(row=5, column=1)
    button3=Button(frame2, text="Сохранить в файл",  width=15, height=1, command=save)
    button3.grid(row=5, column=2)

    win.mainloop()
Menu()