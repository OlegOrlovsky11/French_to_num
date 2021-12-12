from tkinter import *
from tkinter.ttk import *

numbers_0_6 = ['zero', 'un', 'deux', 'trois', 'quatre', 'cinq', 'six']

numbers_wtou_quatre = ['zero', 'un', 'deux', 'trois', 'cinq', 'six']

numbers_0_1 = ['et']

numbers_7_9 = ['sept', 'huit', 'neuf']

numbers_10_16 = ['dix', 'onze', 'douze', 'treize', 'quatorze', 'quinze', 'seize']

numbers_11_16 = ['onze', 'douze', 'treize', 'quatorze', 'quinze', 'seize']

numbers_20_60 = ['vingt', 'trente', 'quarante', 'cinquante', 'soixante']

numbers_20_50 = ['vingt', 'trente', 'quarante', 'cinquante']

numbers_100 = ['cent']

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
    k = 0
    check = (ent_text_num.get().lower()).split(" ")
    check = list(filter(None, check))
    check_len = len(check)
    for m in range(check_len):
        counter.append(check[m])
    ent_arab_num.delete(0)
    ErrorCheck = bool(False)

    for i in range(len(counter)):
        if counter[i] not in numbers_0_6 and counter[i] not in numbers_7_9 and counter[i] not in numbers_10_16 and \
                counter[i] not in numbers_20_60 and counter[i] not in numbers_100 and counter[i] not in numbers_0_1 and counter[i] != 'vingts':
            if counter[i] == 'cents':
                ErrorCheck = True
                Error = "Ошибка орфографии, cent используется без s"
                break
            ErrorCheck = True
            Error = "Встречено неизвестное слово {}".format(counter[i])
            break
        if counter[0] == 'vingts':
            ErrorCheck = True
            Error = "Слово vingts не может использоваться без quatre (Перед vingts должно идти quatre)"
            break
        if counter[i] == 'vingts' and i > 0:
            if counter[i - 1] != 'quatre':
                Error = "Слово vingts не может использоваться без quatre. Уберите s"
                ErrorCheck = True
                break

        if counter[i] == 'zero' and i > 0:
            Error = "Zero не может использоваться вместе с другими символами"
            ErrorCheck = True
            break

        if counter[0] == 'et':
            Error = "Частица et не стоять на первом месте"
            ErrorCheck = True
            break
        if counter[i] == 'et' and i > 0:
            if counter[i - 1] == 'un':
                Error = "Возможно использование только et un, но не un et"
                ErrorCheck = True
                break
            if len(counter) - 1 > i:
                if counter[i + 1] != 'un' :
                    Error = "Частица et может использоваться только с un"
                    ErrorCheck = True
                    break

        for j in range(len(numbers_0_1)):
            if counter[i] == numbers_0_1[j]:
                if i == len(counter) - 1:
                    Error = "Частица et не может использоваться самостоятельно"
                    ErrorCheck = True
                    break
                if (len(counter) - 1 - i) == 1:
                    if counter[i - 1] in numbers_11_16:
                        Error = "Частица et не может использоваться со словом {} 11-19".format(counter[i - 1])
                        ErrorCheck = True
                        break
                    if counter[i + 1] != 'un' and counter[i + 1] != 'onze' and counter[i - 1] not in numbers_11_16 \
                            and not counter[i - 1] in numbers_0_6 and counter[i - 1] not in numbers_7_9 and counter[i - 1] != 'dix':
                        Error = "Частица et может использоваться со словом {} только вмесет с un".format(counter[i - 1])
                        ErrorCheck = True
                        break
                    if counter[i - 1] in numbers_0_6 or counter[i - 1] in numbers_7_9 or counter[i - 1] == 'dix':
                        Error = "Частица et не может использоваться со словом {} 0-19".format(counter[i - 1])
                        ErrorCheck = True
                        break
                    if counter[i + 1] == 'onze' and counter[i - 1] != 'soixante':
                        Error = "Частица et может использоваться со словом {} только вмесет с un".format(counter[i - 1])
                        ErrorCheck = True
                        break



        for j in range(len(numbers_0_6)):
            if counter[i] == numbers_0_6[j]:
                if counter[i] == "zero" and len(counter) > 1:
                    Error = "Zero не может использоваться вместе с другими символами"
                    ErrorCheck = True
                    break

                if i > 0:
                    if counter[i - 1] in numbers_11_16:
                        Error = "Слово {} рязряда едениц не может использоваться после числительных 11-19".format(counter[i])
                        ErrorCheck = True
                        break
                    if counter[i - 1] in numbers_0_6 or counter[i - 1] in numbers_7_9:
                        Error = "Два числа {} и {} единичного разряда идут друг за другом".format(counter[i - 1],
                                                                                                   counter[i])
                        ErrorCheck = True
                        break
                    if counter[i] == 'un' and counter[i - 1] in numbers_20_60:
                        if i > 1:
                            if counter[i] == 'un' and counter[i - 1] == 'vingt' and counter[i - 2] == 'quatre':
                                print('')
                        else:
                            Error = "Вы пропустили et перед un"
                            ErrorCheck = True
                            break
                    if i > 2:
                        if counter[i] == 'un' and counter[i - 1] == 'et' and counter[i - 2] == 'vingt' \
                                and counter[i - 3] == 'quatre':
                            Error = "et un может использоваться только числами 20-70"
                            ErrorCheck = True
                            break

                    if i > 1:
                        if counter[i] == 'un' and counter[i - 1] in numbers_20_60 and counter[i - 2] != 'quatre':
                            Error = "Вы пропустили et перед un"
                            ErrorCheck = True
                            break


                if len(counter) == 2:
                    if counter[i - 1] in numbers_0_1 and counter[i] == 'un':
                        Error = "et un может использоваться только с числами 20-60"
                        ErrorCheck = True
                        break

                for j in range(len(numbers_0_6)):
                    if counter[i] == numbers_0_6[j]:
                        final += j

        for j in range(len(numbers_7_9)):
            if counter[i] == numbers_7_9[j]:
                if counter[i] == "zero" and len(counter) > 1:
                    Error = "Zero не может использоваться вместе с другими символами"
                    ErrorCheck = True
                    break
                if i > 0:
                    if counter[i - 1] in numbers_11_16:
                        Error = "Слово {} разряда едениц не может использоваться с числительными 11-19".format(counter[i])
                        ErrorCheck = True
                        break
                    if counter[i - 1] in numbers_0_6 or counter[i - 1] in numbers_7_9:
                        Error = "Два числа {} и {} единичного разряда идут друг за другом".format(counter[i - 1],
                                                                                                   counter[i])
                        ErrorCheck = True
                        break


                for j in range(len(numbers_7_9)):
                    if counter[i] == numbers_7_9[j]:
                        final += 7 + j

        for j in range(len(numbers_10_16)):
            if counter[i] == numbers_10_16[j]:
                if i > 0:
                    if counter[i - 1] in numbers_10_16:
                        Error = "Два слова {} и {} десятичного разряда идут друг за другом".format(counter[i - 1],
                                                                                                    counter[i])
                        ErrorCheck = True
                        break
                    if i > 1:
                        if counter[i - 1] in numbers_20_60:
                            if counter[i - 1] == 'vingt' and counter[i - 2] == 'quatre':
                                print('')
                            elif counter[i - 1] == 'soixante':
                                print("")
                            else:
                                Error = "Два слова {} и {} десятичного разряда идут друг за другом".format(
                                    counter[i - 1],
                                    counter[i])
                                ErrorCheck = True
                                break
                    if counter[i - 1] in numbers_20_60:
                        if counter[i - 1] == 'soixante' and counter[i] in numbers_10_16:
                            print("")
                        elif counter[0] == 'quatre' and len(counter) > 2:
                            if counter[i - 1] == 'vingts':
                                print("")
                        elif i > 1:
                            if counter[i] == 'dix' and counter[i - 1] == 'vingt' and counter[i - 2] == 'quatre':
                                print('')
                        else:
                            Error = "Два слова {} и {} десятичного разряда идут друг за другом".format(counter[i - 1],
                                                                                                        counter[i])
                            ErrorCheck = True
                            break
                        if i > 1:
                            if counter[i] == 'dix' and counter[i - 1] in numbers_20_60:
                                if counter[i - 1] == 'soixante':
                                    print('')
                                elif counter[i - 1] == 'vingt' and counter[i - 2] == 'quatre':
                                    print('')
                                elif i > 2:
                                    if counter[i] == 'dix' and counter[i - 1] == 'vingt':
                                        if counter[i - 3] == 'quatre':
                                            if counter[i - 2] in numbers_0_6 or counter[i - 2] in numbers_7_9:
                                                Error = "Слово {} еденичного разряда стоит перед словом {} десятичного разряда".format(
                                                    counter[i - 2], counter[i - 1])
                                                ErrorCheck = True
                                                break
                                            elif counter[i - 2] in numbers_10_16 or counter[i - 2] in numbers_20_60:
                                                Error = "Два слова {} и {} десятичного4 разряда идут друг за другом".format(
                                                    counter[i - 1], counter[i - 1])
                                                ErrorCheck = True
                                                break
                                else:
                                    Error = "Два слова {} и {} десятичного разряда идут друг за другом".format(counter[i - 1], counter[i])
                                    ErrorCheck = True
                                    break
                            if len(counter) - i > 1:
                                if counter[i - 1] == 'vingt' and counter[i - 2] == 'quatre' and counter[i + 1] in numbers_0_6:
                                    Error = "После слова {} могут использоваться только слова 7-9".format(counter[i])
                                    ErrorCheck = True
                                    break

                    if len(counter) == i + 1:
                        if counter[i - 1] in numbers_0_6 or counter[i - 1] in numbers_7_9:
                            Error = "Слово {} десятичного разряда стоит после слова {} еденичного разряда".format(
                                counter[i], counter[i - 1])
                            ErrorCheck = True
                            break
                    if counter[i - 1] in numbers_0_6 or counter[i - 1] in numbers_7_9:
                        Error = "Слово {} еденичного разряда стоит перед словом {} десятичного разряда".format(
                            counter[i - 1], counter[i])
                        ErrorCheck = True
                        break

                if len(counter) > i + 1:
                    if counter[i] == 'dix' and counter[i + 1] in numbers_0_6:
                        Error = "Слово {}, меньшее 7 не может использоваться со словом {}".format(counter[i + 1], counter[i])
                        ErrorCheck = True
                        break
                if len(counter) > 2 and counter[i] == 'dix' and (i+1 != len(counter)):
                    if counter[i - 1] == 'soixante' and (
                            counter[i + 1] in numbers_0_6):
                        Error = "После слова {} могут использоваться только слова 7-9".format(counter[i])
                        #Error = "Послеrr {} десятичного разряда должно стоять число 11-16".format(counter[i - 1])
                        ErrorCheck = True
                        break
                if i > 1:
                    if counter[i] in numbers_11_16 and counter[i - 1] in numbers_20_50:
                        Error = "Два слова {} и {} десятичного разряда идут друг за другом".format(counter[i-1], counter[i])
                        ErrorCheck = True
                        break


                if i == 1:
                    if counter[i] == 'dix' and counter[i - 1] == 'vingt':
                        Error = "Два слова {} и {} десятичного разряда идут друг за другом".format(counter[i - 1],
                                                                                                   counter[i])
                        ErrorCheck = True
                        break
                for j in range(len(numbers_10_16)):
                    if counter[i] == numbers_10_16[j]:
                        final += 10 + j

        for j in range(len(numbers_20_60)):
            if counter[i] == numbers_20_60[j] or counter[i] == 'vingts':
                if i > 0:
                    if i + 1 == len(counter):
                        if counter[i - 1] in numbers_0_6 or counter[i - 1] in numbers_7_9:
                            if (counter[i] == 'vingt' or counter[i] == 'vingts') and counter[i - 1] == 'quatre':
                                print("")
                            else:
                                Error = "Слово {} десятичного разряда стоит после слова {} еденичного разряда".format(
                                    counter[i], counter[i - 1])
                                ErrorCheck = True
                                break
                    if counter[i] == 'vingts' or counter[i] == 'vingt':
                        if counter[i - 1] in numbers_wtou_quatre or counter[i - 1] in numbers_7_9:
                            Error = "Слово {} еденичного разряда стоит перед словом {} десятичного разряда".format(
                                counter[i - 1], counter[i])
                            ErrorCheck = True
                            break
                        if i > 1:
                            if counter[i - 1] == 'quatre' and (counter[i - 2] in numbers_10_16 or counter[i - 2] in numbers_20_60):
                                Error = "Слово {} десятичного разряда идет перед словом {} еденичного разряда".format(counter[i - 2], counter[i - 1])
                                ErrorCheck = True
                                break
                        if i + 1 != len(counter):
                            if counter[i] == 'vingts' and (counter[i + 1] in numbers_0_6 or numbers_7_9):
                                Error = "После слова {} не может стоять ничего (используйте vingt)".format(counter[i])
                                ErrorCheck = True
                                break
                        if i + 1 != len(counter):
                            if counter[i - 1] == 'quatre' and counter[i] == 'vingt' and (counter[i + 1] in numbers_0_6 or counter[i + 1] in numbers_7_9 or counter[i + 1] in numbers_10_16):
                                final += 56
                        if i+1 == len(counter):
                            if counter[i] == 'vingt' and counter[i - 1] == 'quatre':
                                Error = "Вы пропусти s в слове {}".format(counter[i])
                                ErrorCheck = True
                                break
                        if i + 1 == len(counter):
                            if counter[i] == 'vingt' and (counter[i - 1] in numbers_0_6 or counter[i - 1] in numbers_7_9):
                                Error = "Слово {} еденичного разряда стоит перед словом {} десятичного разряда".format(
                                    counter[i - 1], counter[i])
                                ErrorCheck = True
                                break


                    elif counter[i] != 'vingts' or counter[i] != 'vingt':
                        if counter[i - 1] in numbers_0_6 or counter[i - 1] in numbers_7_9:
                            Error = "Слово {} еденичного разряда стоит перед словом {} десятичного разряда".format(
                                counter[i - 1], counter[i])
                            ErrorCheck = True
                            break
                    if counter[i - 1] in numbers_20_60:
                        Error = "Два слова {} и {} десятичного разряда идут друг за другом".format(counter[i - 1],
                                                                                                    counter[i])
                        ErrorCheck = True
                        break
                    if counter[i - 1] in numbers_10_16:
                        Error = "Два слова {} и {} десятичного разряда идут друг за другом".format(counter[i - 1],
                                                                                                     counter[i])
                        ErrorCheck = True
                        break
                    if counter[i - 1] in numbers_0_6 or counter[i - 1] in numbers_7_9:
                        if counter[i - 1] == 'quatre' and counter[i] == 'vingts':
                            final += 76
                            break
                        elif counter[i - 1] != 'quatre' and counter[i] != 'vingt' and (counter[i + 1] not in numbers_0_6 or counter[i + 1] not in numbers_7_9):
                            Error = "Слово {} еденичного разряда стоит перед словом {} десятичного разряда".format(
                                counter[i - 1], counter[i])
                            ErrorCheck = True
                            break



                    if len(counter) - 1 == i:
                        if counter[i - 1] in numbers_0_6 or counter[i - 1] in numbers_7_9:
                            if counter[i - 1] != 'quatre' and counter[i] != 'vingts':
                                Error = "Слово {} десятичного разряда стоит после слова {} еденичного разряда".format(
                                    counter[i], counter[i - 1])
                                ErrorCheck = True
                                break

                    if counter[i - 1] in numbers_0_6 or counter[i - 1] in numbers_7_9:
                        if counter[i - 1] != 'quatre' and counter[i] != 'vingts':
                            Error = "Слово {} еденичного разряда стоит перед словам {} десятичного разряда".format(
                                counter[i - 1], counter[i])
                            ErrorCheck = True
                            break

                for j in range(len(numbers_20_60)):
                    if counter[i] == numbers_20_60[j]:
                        final += (j + 2) * 10

        for j in range(len(numbers_100)):
            if counter[i] == numbers_100[j]:
                if counter[i] in numbers_100:
                    k += 1
                if k > 1:
                    Error = "Слово cent разряда сотней используется больше одного раза"
                    ErrorCheck = True
                    break
                if i > 0:
                    if counter[i - 1] in numbers_10_16 or counter[i - 1] in numbers_20_60:
                        Error = "Слово {} десятичного разряда стоит перед словом {} разряда сотней".format(
                            counter[i - 1], counter[i])
                        ErrorCheck = True
                        break
                if i > 1:
                    if counter[0] in numbers_10_16 or counter[0] in numbers_20_60:
                        Error = "Слово {} десятичного разряда не может стоять раньше слова {} разряда сотней".format(
                            counter[0], counter[i])
                        ErrorCheck = True
                        break
                if i > 2:
                    if counter[i - 1] == 'un' and counter[i - 2] =='et' and (counter[i - 3] in numbers_0_6 or counter[i - 3] in numbers_7_9):
                        Error = "Частица et не может использоваться со словом {} разряда едениц".format(counter[i - 3])
                        ErrorCheck = True
                        break
                if i > 2:
                    if counter[i - 2] in numbers_10_16 or counter[i - 2] in numbers_20_60:
                        Error = "Слово {} разряда десятков стоит перед словом {} разрядка сотен".format(counter[i - 2], counter[i])
                        ErrorCheck = True
                        break
                if len(counter) - i > 2:
                    if counter[i + 1] == 'et' and counter[i + 2] == 'un':
                        Error = "Слово {} разряда сотней может использоваться только с un".format(counter[i])
                        ErrorCheck = True
                        break
                if counter[0] in numbers_0_6 and counter[1] in numbers_100:
                    for j in range(len(numbers_0_6)):
                        if counter[0] == numbers_0_6[j]:
                            final += j * 100 - j
                elif counter[0] in numbers_7_9 and counter[1] in numbers_100:
                    for j in range(len(numbers_7_9)):
                        if counter[0] == numbers_7_9[j]:
                            final += (j + 7) * 100 - (j + 7)
                if counter[0] in numbers_100:
                    final += 100

    if ErrorCheck:
        ent_old_rus_num.delete(0)
        ent_arab_num.delete(0)
        ent_errors.insert(0, Error)
    if not ErrorCheck:
        ent_arab_num.insert(0, final)
        old_Rus()


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