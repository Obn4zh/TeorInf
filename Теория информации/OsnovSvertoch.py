import numpy as np
import binascii
from tkinter import *
import tkinter.messagebox as mb

n=int(input("Введите количество сумматоров: "))
posled=input("Введите последовательность: ")


def text_to_bits(posled, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(posled.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


spisok_text_to_bit = text_to_bits(posled)
spis_posled=[]
for i in range(len(spisok_text_to_bit)):
    spis_posled.append(spisok_text_to_bit[i])


print(spisok_text_to_bit)


print("Введённая последовательность в бинарном представлении: ",spis_posled)

poFactu=[]
registr=np.zeros(3)

dvoinoySpisElemIndex=[]
for i in range(n):
    spiselemindex=[]
    elemindex=input("Введите элементы для сумматора через (,): ")
    spiselemindex=elemindex.split(",")
    dvoinoySpisElemIndex.append(spiselemindex)


print("Индексы слогаемых: ",dvoinoySpisElemIndex)
print("Состояния регистра:")
print(registr)