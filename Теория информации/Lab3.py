import os
import matplotlib.image as img
import matplotlib.pyplot as plt
import random

def oshibaisya(opa):
    k=0
    opa="{0:08b}".format(opa)
    while k <= n:
        rng=list(range(0,8))
        index=random.choice(rng)
        if opa[index]=="1":
            zamena="0"
        else:
            zamena="1"

        opa =opa[:index] + zamena + opa[index+1:]
        k=k+1

    return int(opa[:],2)

#Первая часть
Way="D:\\ТеорИнф3Курс\\1.jpeg"
#os.system("Way")
photo=img.imread(Way)

#Вторая часть
razmer=photo.shape

y=razmer[0]
x=razmer[1]

for i in range(y):
    for j in range(x):
        n=1
        photo[i][j][0] = int(oshibaisya(photo[i][j][0]))
        photo[i][j][1] = int(oshibaisya(photo[i][j][1]))
        photo[i][j][2] = int(oshibaisya(photo[i][j][2]))
print(photo)
plt.imshow(photo)
plt.axis("off")
plt.show()


#Третья часть


