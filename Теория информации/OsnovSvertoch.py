import numpy as np
import binascii
from tkinter import *
import tkinter.messagebox as mb

dvoinoySpisElemIndex=[]


def summatory():
    global elemindex
    global dvoinoySpisElemIndex
    global schet_zapyat
    global schet_chisel

    elemindex=text3.get()
    schet_zapyat=0
    schet_chisel=0

    dvoinoySpisElemIndex.append(elemindex.split(","))

    for i in range(len(elemindex)):
        if elemindex[i].isdigit():
            schet_chisel+=1
        if elemindex[i]==",":
            schet_zapyat+=1
    if schet_chisel - schet_zapyat!=1:
        mb.showwarning("Предупреждение", "Неверно введенные сумматоры\nВведите другие")
        elemindex=""
        dvoinoySpisElemIndex.clear()
        text3.delete(0, END)

    if i % 2 == 0:
        if int(elemindex[i]) > 2:
            mb.showwarning("Предупреждение", "Неверно введенные сумматоры\nВведите другие")
            dvoinoySpisElemIndex.clear()
            text3.delete(0, END)

    text3.delete(0, END)

def kolsum():
    global n
    dvoinoySpisElemIndex.clear()
    n = ""
    n = text2.get()
    if not n.isdigit():
        mb.showwarning("Предупреждение", "Сумматор должен быть числом")
    else:
        n = int(n)


def ooo():
    global zakodir
    global spisok_text_to_bit


    posled=text1.get()
    if len(posled)==0:
        mb.showwarning("Предупреждение", "Введите последовательность")
        text2.delete(0, END)
        dvoinoySpisElemIndex.clear()

    print(posled)



    def text_to_bits(posled, encoding='utf-8', errors='surrogatepass'):
        bits = bin(int(binascii.hexlify(posled.encode(encoding, errors)), 16))[2:]
        return bits.zfill(8 * ((len(bits) + 7) // 8))


    spisok_text_to_bit = text_to_bits(posled)
    spis_posled=[]
    for i in range(len(spisok_text_to_bit)):
        spis_posled.append(spisok_text_to_bit[i])


    print(spisok_text_to_bit)


    print("Введённая последовательность в бинарном представлении: ",spis_posled)


    registr=np.zeros(3)
#проверка на корректность введенных сумматоров


    if len(dvoinoySpisElemIndex)>n:
        mb.showwarning("Предупреждение", "Введено больше сумматоров, чем заявлялось")
        dvoinoySpisElemIndex.clear()


    elif len(dvoinoySpisElemIndex)<n:
        mb.showwarning("Предупреждение", "Введено меньше сумматоров, чем заявлялось")
        dvoinoySpisElemIndex.clear()



    print("Индексы слогаемых: ",dvoinoySpisElemIndex)
    print("Состояния регистра:")
    print(registr)

    poFactu=[]
    for i in range(len(spis_posled)):
        registr=np.delete(registr,2)
        registr=np.insert(registr,0,spis_posled[i])
        print(registr)

        for j in range(len(dvoinoySpisElemIndex)):
            spisElemSlogaem=[]
            for k in dvoinoySpisElemIndex[j]:
                spisElemSlogaem.append(registr[int(k)])
            a=sum(spisElemSlogaem)
            poFactu.append(a%2)

    for i in range(len(poFactu)):
        poFactu[i]=int(poFactu[i])
        poFactu[i]=str(poFactu[i])

    zakodir=[]

    for i in range(0,len(poFactu),n):
        zakodir.append("".join(poFactu[i:i+n]))

    zakodirstr="".join(zakodir)
    print("Закодированная последовательность: ", zakodirstr)
    print(zakodir)



    lbl = Label(text=zakodirstr, bg='#98FB98', bd=5, font=2)
    lbl.pack()
    lbl.place(x=120, y=100)


    #ДЕКОДИРОВАНИЕ
def decodir():
    registr = []
    kol_razryadov = 0

    decodir_str = ''
    for i in dvoinoySpisElemIndex:
        if kol_razryadov < int(max(i)):
            kol_razryadov = int(max(i))

    for i in range(kol_razryadov + 1):
        registr.append(0)

    def nolVregister():
        for i in reversed(range(len(registr))):
            registr[i] = registr[i - 1]
        registr[0] = 0
        return registr

    def ProverochBitki():
        print("!!!!!!!!!!!!!!",registr)
        global proverochnie_bits
        proverochnie_bits = ''
        for j in range(len(dvoinoySpisElemIndex)):
            c = 0
            for m in range(len(dvoinoySpisElemIndex[j])):
                c += registr[int(dvoinoySpisElemIndex[j][m])]
            if c % 2 == 1:
                proverochnie_bits += ''.join('1')
            elif c % 2 == 0:
                proverochnie_bits += ''.join('0')
        return proverochnie_bits

    for i in range(len(zakodir)):
        nolVregister()
        ProverochBitki()
        if proverochnie_bits != zakodir[i]:
            registr[0] = 1
            decodir_str += ''.join('1')
        elif proverochnie_bits == zakodir[i]:
            decodir_str += ''.join('0')
    print("Декодированная последовательность в бинарном представлении: ",decodir_str)


    def text_from_bits(binstring, encoding='utf-8', errors='surrogatepass'):
        l = int(binstring, 2)
        return int2bytes(l).decode(encoding, errors)


    def int2bytes(i):
        hex_string = '%x' % i
        l = len(hex_string)
        return binascii.unhexlify(hex_string.zfill(l + (l & 1)))

    decodir_poFactu = text_from_bits(decodir_str)

    print("Декодированная последовательность: ",decodir_poFactu)
    lbld = Label(text=decodir_poFactu, bg='#98FB98', bd=5, font=8)
    lbld.pack()
    lbld.place(x=120, y=150)



window = Tk()
window.title("Свёрточные кодики")
window.geometry("800x250+600+200")

lbl1 = Label(text="Введите текст")
lbl1.pack()
lbl1.place(x=1)

text1 = Entry(width=100)
text1.pack()

lbl2 = Label(text="Количество сумматоров")
lbl2.pack()
lbl2.place(x=1, y=20)

text2 = Entry(width=80)
text2.pack()

lbl3 = Label(text="Введите сумматоры\n(через запятую)")
lbl3.pack()
lbl3.place(x=1, y=40)

text3 = Entry(width=80)
text3.pack()

btn_clear=Button(text="жмяк",command=summatory)
btn_clear.pack()
btn_clear.place(x=290,y=60)

btn_kol=Button(text="подтвердить",command=kolsum)
btn_kol.pack()
btn_kol.place(x=660,y=20)

btn=Button(text="кодировать",command=ooo)
btn.pack()
btn.place(x=5,y=100)
btn0=Button(text="декодировать",command=decodir)
btn0.pack()
btn0.place(x=5,y=150)


lbl = Label(text=0, bg='#98FB98',bd=5,font=8)
lbl.pack()
lbl.place(x=120, y=100)

lbld = Label(text=0, bg='#98FB98',bd=5,font=8)
lbld.pack()
lbld.place(x=120, y=150)

window.mainloop()