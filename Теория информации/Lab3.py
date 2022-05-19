# НА I ОСТАНОВИЛСЯ

import os
import matplotlib.image as img
import matplotlib.pyplot as plt
import random
import numpy as np
from sympy import *
import math

def oshibaisya2(opa1):

    rng=list(range(0,19))
    rng1=random.sample(rng,2)
    for i in range(len(rng1)):
        if (opa1[rng1[i]])=="1":
            opa1 = opa1[:rng1[i]] + "0" + opa1[rng1[i] + 1:]
        else:
            opa1 = opa1[:rng1[i]] + "1" + opa1[rng1[i] + 1:]

    return (opa1)

def oshibaisya(opa):
    global kolOsh
    k=0
    opa="{0:08b}".format(opa)
    while k <= kolOsh:
        rng=list(range(0,8))
        index=random.choice(rng)
        if opa[index]=="1":
            zamena="0"
        else:
            zamena="1"

        opa =opa[:index] + zamena + opa[index+1:]
        k=k+1

    return int(opa[:],2)


def oshibaisya2(opa1):
    k = 0
    while k <= kolosh-1:
        rng=list(range(0,19))
        index=(random.choice(rng))
        if opa1[index]=="1":
            zamena="0"
        else:
            zamena="1"

        opa1=opa1[:index] + zamena + opa1[index+1:]
        k=k+1
    return (opa1)

#Первая часть
Way="D:\ТеорИнф3Курс\для тестов.bmp"
#os.system("Way")
photo=img.imread(Way)

#Вторая часть
# razmer=photo.shape
#
# y=razmer[0]
# x=razmer[1]
#
# for i in range(y):
#     for j in range(x):
#         kolOsh=2
#         photo[i][j][0] = int(oshibaisya(photo[i][j][0]))
#         photo[i][j][1] = int(oshibaisya(photo[i][j][1]))
#         photo[i][j][2] = int(oshibaisya(photo[i][j][2]))
# print(photo)
# plt.imshow(photo)
# plt.axis("off")
# plt.show()

#Третья часть
matrix = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0],
 [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
 [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0],
 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
 [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
 [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0]])


# УДАЛЕНИЕ ИЗ МАТРИЦЫ СТОЛБЦОВ ДЛЯ ЕДИНИЧНОЙ
tutu = []
column = 0
column1 = 0
ed = np.eye(len(matrix))
for i in range(len(matrix)):
    column = ed[:,i]
    for j in range(len(matrix[0])):
        column1 = matrix[:,j]
        if (column == column1).all():
            tutu.append(j)
            break
matrix = np.delete(matrix,np.s_[tutu],axis=1)

matrix2 =np.array ([
 [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0],
 [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
 [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0],
 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
 [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
 [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0]])
print("Gsys =\n", matrix2)
matrix1 = np.transpose(matrix)
matrix3 = np.c_[matrix1, np.eye(len(matrix1))]
print("Hsys=\n", matrix3)
k = len(matrix2)
n = len(matrix2[0])
print("k = ", k)
print("n = ", n)
hihi = []
I = []
for i in range(0, 2 ** k):
    hihi.append([int(i)])
m = []
for i in range(0, len(hihi)):
    haha = np.binary_repr(hihi[i][0], width=k)
    for j in range(0, len(haha)):
        m.append(int(haha[j]))
    I.append(m)
    m = []

I = np.array(I)
print("")
print("i=\n", I)
print(len(I))
matrix_c = np.dot(I, matrix2)

for i in range(len(matrix_c)):
    for j in range(len(matrix_c[i])):
        if matrix_c[i][j] % 2 == 0:
            matrix_c[i][j] = 0
        else:
            matrix_c[i][j] = 1
print("")
print("c=\n", matrix_c)
print("")
d = np.sum(matrix_c, axis=1)
print("wth =\n", d)
print("")
d = int(min(d[1:]))
print("d =", d)

x = Symbol('x')
t = solve(2 * x + 1 - d, x)
t[0] = math.floor(t[0])
Ro = solve(x + 1 - d, x)
print("t =", t[0])
print("Ro = ", Ro[0])

HsysT = np.transpose(matrix3)


pum = []
for i in range(2**(19)):
    s = bin(i)[2:]
    pum.append(s.zfill(19))
pum2 = []

for i in range(len(pum)):
    if pum[i].count("1") == 1:
        pum2.append(pum[i])
    if pum[i].count("1") == 2:
        pum2.append(pum[i])
print(pum2)
pum3=[]
pum4=[]
for i in range(len(pum2)):
    for j in range(len(pum2[i])):
            pum3.append(int(pum2[i][j]))
            pum4.append(pum3)
            pum3=[]

ogoSpis2=np.array(pum4)
# !!!!!!!!!!!!
e = ogoSpis2.reshape(-1, 19)

s = np.dot(e, HsysT)

for i in range(len(s)):
    for j in range(len(s[i])):
        if s[i][j] % 2 == 0:
            s[i][j] = 0
        else:
            s[i][j] = 1

print("S =\n", s)
print("e =\n", e)
print("HsysT =\n", HsysT)

Way="D:\ТеорИнф3Курс\для тестов.bmp"
photo=img.imread(Way)
infslov=[]
razmer1=photo.shape
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",razmer1)

l=[]
l1=[]
yy=razmer1[0]
xx=razmer1[1]
for i in range(yy):
    for j in range(xx):
        infslov.append("{0:08b}".format(photo[i][j][0]))
        infslov.append("{0:08b}".format(photo[i][j][1]))
        infslov.append("{0:08b}".format(photo[i][j][2]))
infslov=np.array(infslov)
infslov = infslov.reshape(-1, 1)


for i in range(len(infslov)):
    l.append(list(infslov[i][0]))
for i in range(len(l)):
    for j in range(0,8):
        l1.append(int(l[i][j]))
l1=np.array(l1)
l1 = l1.reshape(-1, 8)
print("Инф слова\n",l1)

# S вывод
sss = np.dot(l1, matrix2)
for i in range(len(sss)):
    for j in range(len(sss[i])):
        if sss[i][j] % 2 == 0:
            sss[i][j] = 0
        else:
            sss[i][j] = 1

sss1=[]


for i in range(len(sss)):
    for j in range(len(sss[i])):
      sss1.append(str(sss[i][j]))

sss1=np.array(sss1)
sss1 = sss1.reshape(-1, 19)



sss2=[]

for i in range(len(sss1)):
    sss2.append("".join(sss1[i]))
sss2=np.array(sss2)
sss2=sss2.reshape(-1,1)
Cn=sss2

Vmatrix=[]

for i in range(len(Cn)):
    pipa=oshibaisya2(Cn[i][0])
    Vmatrix.append(pipa)

Vmatrix=np.array(Vmatrix)
Vmatrix=np.reshape(Vmatrix,(len(Vmatrix),1))
VmatrixNuzh=[]
for i in range(len(Vmatrix)):
    VmatrixNuzh.append(list(Vmatrix[i][0]))
for i in range(len(VmatrixNuzh)):
    for j in range(len(VmatrixNuzh[i])):
        VmatrixNuzh[i][j]=int(VmatrixNuzh[i][j])
VmatrixNuzh=np.array(VmatrixNuzh)

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n",VmatrixNuzh)



pupa = []
c1 = []

sSHtrih=[]
decod=[]
iDecod=[]
pp=[]
for j in range(len(VmatrixNuzh)):
    v1 = []
    v = VmatrixNuzh[j].tolist()
    v1=np.array(v)
    s1 = np.dot(v1, HsysT)

    sSHtrih.append(list(s1))

for i in range(len(sSHtrih)):
    for j in range(len(sSHtrih[i])):
        sSHtrih[i][j]=int(sSHtrih[i][j])
        if (sSHtrih[i][j] % 2 == 0):
            sSHtrih[i][j] = 0
        if sSHtrih[i][j] > 1 and sSHtrih[i][j] % 2!=0:
            sSHtrih[i][j]=1

p=0
for i in range(0, len(sSHtrih)):
    for j in range(0,len(s)):
        if (sSHtrih[i] == s[j]).all():
            p = j
            e1 = e[p]
            pp.append(e1)
pp=np.array(pp)

# print("e(nuzh)\n",pp)
print(len(pp))





Cshtrih=np.add(VmatrixNuzh,pp)

for i in range(len(Cshtrih)):
    for j in range(len(Cshtrih[i])):
        if (Cshtrih[i][j] % 2 == 0).all():
            Cshtrih[i][j] = 0
        else:
            Cshtrih[i][j] = 1

print("C`\n",Cshtrih)
print(len(Cshtrih))

print('C\n',matrix_c)
print(len(matrix_c))


lupa=[]
for i in range(0, len(Cshtrih)):
    for j in range(0, len(matrix_c)):
        if (Cshtrih[i] == matrix_c[j]).all():
            lupa.append(I[j])
lupa=np.array(lupa)

print(photo)
iiiiii=[]
print("i\n",lupa)
print(len(lupa))
for i in range(len(lupa)):
    iiiiii.append((int("".join(map(str,lupa[i])),2)))

pom1=[]
pom2=[]
iiiiii=np.array(iiiiii)
for i in range(0,len(iiiiii),3):
    pom1.append(iiiiii[i])
    pom1.append(iiiiii[i+1])
    pom1.append(iiiiii[i+2])
    pom2.append(pom1)
    pom1=[]
Inuzh=[np.array(pom2)]
Inuzh=np.array(Inuzh)
Inuzh=np.reshape(Inuzh,(razmer1))
# print("i (декодир инф слова): \n", Inuzh)

plt.imshow(Inuzh)
plt.axis("off")
plt.show()