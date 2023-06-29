def  KiemTraNhuan(x):
    if (x % 4 == 0 and x % 100 != 0) or x%400 == 0:
        return True
    else:
        return False

x = int(input("Nhap x: "))
y = int(input("Nhap y: "))
n = x
for i in range(x, y+1):
    if(KiemTraNhuan(i)):
        print(i)
