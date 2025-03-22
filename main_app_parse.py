"""Приложение для парсинга hh.ru"""
from modules.parse import parse
from modules.csv_create import create_excel

from tkinter import *
from tkinter import messagebox as mb
import os


win = Tk()
width  = win.winfo_screenwidth()//2-250 # добавить смещение в центр
height = win.winfo_screenheight()//2-200
win.geometry(f'500x400+{width}+{height}')
win.resizable(False,False)

"""Функции"""

def send_request():
    request = en_request.get()
    if request:
        mb.showinfo('Инфо', 'Запрос отправлен\n'
        'Программа не зависла\n'
        'Пожалуйста, подождите')
        parse(vacantion=request, pages=100, per_page=100)
        mb.showinfo('Инфо', 'Файл составлен')
    else:
        mb.showerror('Ошибка', 'Пустой запрос')

def create_file_excel():
    try:
        create_excel()
    except Exception:
        mb.showerror('Ошибка', 'Файл не найден\nПроверьте запрос')
    else:
        mb.showinfo('Инфо', 'Файл excel составлен')

def open_excel():
    try:
        os.startfile('вакансии.xlsx')
    except Exception:
        mb.showerror('Ошибка', 'Файл не найден\nПроверьте запрос')

lb_request = Label(win, text='Запрос:', font=('Arial', 12))       # Лэйбл запрос
lb_request.pack()
en_request = Entry(win, font=('Arial', 12), width=50)             # Поле ввода запроса
en_request.pack()

lb_example = Label(win, text='Пример:\n'
'(python AND junior) OR (python AND стажер)', font=('Arial',12))  # Пример запроса
lb_example.pack()


bt_send = Button(win, text='Отправить\nзапрос', font=('Arial', 12), command=send_request)    # кнопка отправить запрос
bt_send.place(x=200, y=270)
bt_excel = Button(win, text='Создать\nexcel', font=('Arial', 12), command=create_file_excel) # кнопка создать excel
bt_excel.place(x=170, y=320)
bt_open_excel = Button(win, text='Открыть\nexcel', font=('Arial', 12), command=open_excel)   # кнопка открыть excel
bt_open_excel.place(x=247, y=320)


def klick(eve):
    print(f'x: {eve.x} y: {eve.y}')

win.bind('<Button-1>', klick)

win.mainloop()