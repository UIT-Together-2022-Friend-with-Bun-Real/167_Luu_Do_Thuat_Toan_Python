import math
def KhoangCach(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) * (x2- x1) + (y2 - y1)*(y2 - y1))

x1 = float(input("Nhap x1: "))
y1 = float(input("Nhap y1: "))
x2 = float(input("Nhap x2: "))
y2 = float(input("Nhap y2: "))
print("Khoang cach giua hai diem la: ",KhoangCach(x1, y1, x2, y2))