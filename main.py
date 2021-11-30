from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import collections

numbers_0 = ['zero']

numbers_0_6 = ['un', 'deux', 'trois', 'quatre', 'cinq', 'six']

numbers_7_9 = ['sept', 'huit', 'neuf']

numbers_10_16 = ['dix', 'onze', 'douze', 'treize', 'quatorze', 'quinze', 'seize']

numbers_20_60 = ['vingt', 'trente', 'quarante', 'cinquante', 'soixante']


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
    ent_errors.delete(0, END)
    ent_old_rus_num.delete(0, END)
    ent_arab_num.delete(0, END)
    counter = []
    final = 0
    check = (ent_text_num.get()).split(" ")
    check = list(filter(None, check))
    check_len = len(check)
    for m in range(check_len):
        counter.append(check[m])
    ent_arab_num.delete(0)
    ErrorCheck = bool(False)

    for i in range(len(counter)):
        if counter[i] in numbers_0:
            if len(counter) > 1 and counter[i + 1] in numbers_0_6:
                ErrorCheck = True
                Error = "Ноль не может использоваться с другими числами"
                break
            else:
                final = 0


        elif counter[i] in numbers_0_6 or counter[i] in numbers_7_9:
            if (len(counter) > 1 and counter[i - 1] in numbers_0_6) or (
                    len(counter) > 1 and counter[i - 1] in numbers_7_9):
                ErrorCheck = True
                Error = "Числа еденичного разряда {} и {} идут друг за другом".format(counter[i], counter[i - 1])
                break
            else:
                if counter[i] in numbers_0_6:
                    for j in range(len(numbers_0_6)):
                        if counter[i] == numbers_0_6[j]:
                            final += j + 1
                if counter[i] in numbers_7_9:
                    for j in range(len(numbers_7_9)):
                        if counter[i] == numbers_7_9[j]:
                            final += j + 7
        elif counter[i] in numbers_10_16:
            if len(counter) > 1:
                if counter[i - 1] in numbers_10_16:
                    ErrorCheck = True
                    Error = "Числа десятичного разряда {} и {} идут друг за другом".format(counter[i - 1], counter[i])
                    break
                if counter[i - 1] in numbers_20_60 and counter[i - 1] != 'soixante' and counter[i] != 'dix':
                    ErrorCheck = True
                    Error = "Числа десятичного разряда {} и {} идут друг за другом".format(counter[i - 1], counter[i])
                    break
            elif len(counter) > 1 and counter[i] == "dix" and len(counter) != 2: # тут херня
                if counter[i + 1] in numbers_7_9:
                    final += 10
            else:
                for j in range(len(numbers_10_16)):
                    if counter[i] == numbers_10_16[j]:
                        final += j + 10
        elif counter[i] in numbers_20_60:
            if len(counter) > 1:
                if counter[i] == 'soixante' and counter[i + 1] == 'dix':
                    final += 70
                elif counter[i + 1] in numbers_20_60 or counter[i + 1] in numbers_10_16:
                    ErrorCheck = True
                    Error = "Числа десятичного разряда {} и {} идут друг за другом".format(counter[i], counter[i + 1])
                    break
            else:
                for j in range(len(numbers_20_60)):
                    if counter[i] == numbers_20_60[j]:
                        if final == 0:
                            final = (j + 2) * 10
                        else:
                            final += (j + 2) * 10

        else:
            ErrorCheck = True
            Error = "Встречено неизвестное слово {}".format(counter[i])
            break

    if ErrorCheck:
        ent_old_rus_num.delete(0)
        ent_arab_num.delete(0)
        ent_errors.insert(0, Error)
    if not ErrorCheck:
        ent_arab_num.insert(0, final)
        old_Rus()


# except Exception as err:
#    ent_errors.insert(0, "Проверьте корректность ввода, возможно вы пропустили - ")


window = Tk()

about = []
resultat = []
window.geometry("2048x650")

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

btn = Button(master=frm_form, text="Convert", command=clicked, width=10)
btn.grid(row=8, column=0)

window.mainloop()
