import os
import matplotlib.image as img
import matplotlib.pyplot as plt
import random

def oshibaisya(opa):
    opa="{0:08b}".format(opa)
    rng=list(range(0,8))
    index=random.choice(rng)
    if opa[index]=="1":
        zamena="0"
    else:
        zamena="1"

    opa =opa[:index] + zamena + opa[index+1:]


    return int(opa[:],2)

#os.system("D:\ТеорИнф3Курс\смотрю.jpg")

photo=img.imread("D:\ТеорИнф3Курс\смотрю.jpg")

razmer=photo.shape

y=razmer[0]
x=razmer[1]

for i in range(y):
    for j in range(x):
        photo[i][j][0] = int(oshibaisya(photo[i][j][0]))
        photo[i][j][1] = int(oshibaisya(photo[i][j][1]))
        photo[i][j][2] = int(oshibaisya(photo[i][j][2]))


print(photo)
plt.imshow(photo)
plt.axis("off")
plt.show()


