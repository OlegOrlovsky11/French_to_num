from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import collections

number_0_9 = []

number_10_19 = []

number_20_99 = []

number_100_1000 = []


def old_Rus():
    ent_old_rus_num.delete(0, END)
    if len(ent_arab_num.get()) != 0:
        i = int(ent_arab_num.get())
        a = []
        while i > 0:
            if i >= 500:
                i -= 500
                a.append("Ф")
                continue
            if i >= 100:
                i -= 100
                a.append("Р")
                continue
            if i >= 30:
                i -= 30
                a.append("Л")
                continue
            if i >= 9:
                i -= 9
                a.append("Д")
                continue
            if i >= 8:
                i -= 8
                a.append("И")
                continue
            if i >= 2:
                i -= 2
                a.append("В")
                continue
            if i >= 1:
                i -= 1
                a.append("А")
                continue
        ent_old_rus_num.insert(0, "".join(a))


def clicked():
    try:
        ent_errors.delete(0, END)
        ent_old_rus_num.delete(0, END)
        ent_arab_num.delete(0, END)
        counter = []
        check = (ent_text_num.get()).split(" ")
        check = list(filter(None, check))
        check_len = len(check)
        for m in range(check_len):
            counter.append(check[m])
        ent_arab_num.delete(0)
        length_counter = len(counter)

        ErrorCheck = bool(False)
        for i in range(length_counter):
            print(counter[i])





















    except Exception as err:
        ent_errors.insert(0, "Проверьте корректность ввода, возможно вы пропустили - ")


window = Tk()



about = []
resultat = []
window.geometry("1920x1024")

window.title("ConvertToNumFrench")

frm_form = Frame(relief=SUNKEN, borderwidth=3)
frm_form.pack()

text_num = Label(master=frm_form, text="Текстовое представление числа", font=('Times New Roman', 50))
ent_text_num = Entry(master=frm_form, width=95, font=('Times New Roman', 40))
text_num.grid(row=0, column=0, sticky='nwes')
ent_text_num.grid(row=1, column=0, sticky='nwes')

arab_num = Label(master=frm_form, text="Числовое представление (Арабские цифры)", font=('Times New Roman', 50))
ent_arab_num = Entry(master=frm_form, width=95, font=('Times New Roman', 40))
arab_num.grid(row=2, column=0, sticky='nwes')
ent_arab_num.grid(row=3, column=0, sticky='nwes')

old_rus_num = Label(master=frm_form, text="Числовое представление (Страрорусские цифры)", font=('Times New Roman', 50))
ent_old_rus_num = Entry(master=frm_form, width=95, font=('Times New Roman', 40))
old_rus_num.grid(row=4, column=0, sticky='nwes')
ent_old_rus_num.grid(row=5, column=0, sticky='nwes')

errors = Label(master=frm_form, text="Ошибки", font=('Times New Roman', 50))
ent_errors = Entry(master=frm_form, width=95, font=('Times New Roman', 35))
errors.grid(row=6, column=0, sticky='nwes')
ent_errors.grid(row=7, column=0, sticky='nwes')

btn = Button(master=frm_form, text="Convert", command=clicked, width = 10)
btn.grid(row=8, column=0)

window.mainloop()