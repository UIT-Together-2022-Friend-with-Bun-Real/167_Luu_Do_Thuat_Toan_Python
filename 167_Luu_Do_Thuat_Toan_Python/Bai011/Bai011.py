import math
def DienTich(x1, y1, x2, y2, x3, y3):
    a = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
    b = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3)) 
    c = math.sqrt((x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y1))
    p = float((a + b + c) / 2)
    return math.sqrt(p*(p-a)*(p-b)*(p-c))
x1 = float(input("Nhap x1: "))
y1 = float(input("Nhap y1: "))
x2 = float(input("Nhap x2: "))
y2 = float(input("Nhap y2: "))
x3 = float(input("Nhap x3: "))
y3 = float(input("Nhap y3: "))
print("Dien tich cua tam giac la: ", DienTich(x1, y1, x2, y2, x3, y3))