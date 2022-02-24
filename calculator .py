from tkinter import *
from sympy import *
import re
import tkinter.messagebox as mb

def ooo():
    def Evk(delitel, mod):
        if delitel == 0:
            return (mod, 0, 1)
        else:
            div, x, y = Evk(mod % delitel, delitel)
        return (div, y - (mod // delitel) * x, x)

    elemspis = list()
    prim = text1.get()

    for i in range(len(prim)):
        if prim[i] == "^":
            mb.showwarning("Предупреждение", "Для возведения в степень не используйте ^")
            lbl = Label(text="0", bg='#98FB98')
            lbl.pack()
            lbl.place(x=50, y=70)

    mod = text2.get()

    if len(prim) == len(mod) == 0:
        mb.showwarning("Предупреждение", "Заполните все строки")
    if len(prim)  == 0:
        mb.showwarning("Предупреждение", "Заполните все строки")
    if len(mod) == 0:
        mb.showwarning("Предупреждение", "Заполните все строки")

    schet = 0
    schet1 = 0
    for i in range(len(prim)):
        if prim[i] == "(":
            schet += 1
        if prim[i] == ")":
            schet1 += 1
    if schet != schet1:
        mb.showwarning("Предупреждение", "Количество открытых и закрытых скобок должно совпадать")
        lbl = Label(text="0", bg='#98FB98')
        lbl.pack()
        lbl.place(x=50, y=70)

    # Раскрывакм скобки
    raskprim = expand(prim)
    prim = str(raskprim)


    foundElem = re.findall("[(0-9+*/\-)]", prim)
    for i in prim:
        elemspis.append(i)
    if not elemspis == foundElem:
        mb.showwarning("Предупреждение", "Используйте только цифры и знаки операций")
        lbl = Label(text="0", bg='#98FB98')
        lbl.pack()
        lbl.place(x=50, y=70)




    if not isprime(int(mod)):
        mb.showwarning("Предупреждение", "mod должен быть простым числом")
        lbl = Label(text="0", bg='#98FB98')
        lbl.pack()
        lbl.place(x=50, y=70)

    prim1 = re.split("([(*\-+/)])", prim)

    for i in range(len(prim1)):
        if prim1[i] == "/" and prim1[i + 1] == "0":
            mb.showwarning("Предупреждение", "Делить на 0 нельзя")
            lbl = Label(text="0", bg='#98FB98')
            lbl.pack()
            lbl.place(x=50, y=70)

    print(prim1)


    for i in range(len(prim1)):

        if prim1[i] == "/":
            delitel = prim1[i + 1]
            print(delitel)
            nodi = Evk(int(delitel), int(mod))

            print(f'Делитель равен {nodi[0]}, x = {nodi[1]}, y = {nodi[2]}')
            obr = nodi[1]
            prim1[i] = '*'
            prim1[i + 1] = str(obr)
            prim = "".join(prim1)
    otvet = eval(prim)
    otvet = otvet % int(mod)
    print(otvet)

    lbl = Label(text=otvet, bg='#98FB98')
    lbl.pack()
    lbl.place(x=50, y=70)


window = Tk()
window.title("Калькулятор")
window.geometry("482x150+600+200")

lbl1 = Label(text="Выражение")
lbl1.pack()
lbl1.place(x=1)

lbl2 = Label(text="mod")
lbl2.pack()
lbl2.place(x=1, y=20)

lbl2 = Label(text="Ответ:")
lbl2.pack()
lbl2.place(x=1, y=70)

lbl = Label(text="0", bg='#98FB98')
lbl.pack()
lbl.place(x=50, y=70)

btn = Button(text="Расчитать", command=ooo)
btn.pack()
btn.place(x=1, y=120)
text1 = Entry(width=55)
text1.pack()
text2 = Entry(width=55)
text2.pack()

window.mainloop()