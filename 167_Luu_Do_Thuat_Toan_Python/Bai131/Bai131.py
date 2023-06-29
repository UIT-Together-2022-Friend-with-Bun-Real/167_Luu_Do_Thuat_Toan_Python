import math
def DoDai(x1,y1,x2,y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2)*(y1 - y2))

xA = float(input("Nhap xA: "))
yA = float(input("Nhap yA: "))
xB = float(input("Nhap xB: "))
yB = float(input("Nhap yB: "))
xC = float(input("Nhap xC: "))
yC = float(input("Nhap yC: "))
a = DoDai(xA, yA, xB, yB)
b = DoDai(xA, yA, xC, yC)
c = DoDai(xB, yB, xC, yC)
kq = ""
if a + b > c and a + c > b and b + c > a:
    kq = "La tam giac"
else:
    kq = "Khong la tam giac"
print(kq)

