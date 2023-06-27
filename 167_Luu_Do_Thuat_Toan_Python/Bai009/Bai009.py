import math
n=int(input("Nhap so canh cua da giac deu: "))
r=float(input("Nhap ban kinh duong tron ngoai tiep da giac: "))
s=float(n*r*r*math.sin(2*math.pi/n)/2)
print("Dien tich da giac deu noi tiep duong tron la: ", s)
