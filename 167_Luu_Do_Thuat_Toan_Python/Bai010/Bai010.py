import math
x1 = float(input("Nhap toa do x1 cua dinh A: "))
y1 = float(input("Nhap toa do y1 cua dinh A: "))
x2 = float(input("Nhap toa do x2 cua dinh B: "))
y2 = float(input("Nhap toa do y2 cua dinh B: "))
x3 = float(input("Nhap toa do x3 cua dinh C: "))
y3 = float(input("Nhap toa do y3 cua dinh C: "))

a = math.sqrt((x3-x2)*(x3-x2)+(y3-y2)*(y3-y2))
b = math.sqrt((x3-x1)*(x3-x1)+(y3-y1)*(y3-y1))
c = math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
p = a + b + c
print("Chu vi cua tam giac la : ", p)

