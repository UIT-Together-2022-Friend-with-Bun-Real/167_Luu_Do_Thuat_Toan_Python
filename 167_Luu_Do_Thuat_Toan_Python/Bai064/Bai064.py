n = int(input("Nhap n: "))
lc = n % 10
t = n
while t != 0:
    dv = t % 10
    if (dv>lc):
        lc = dv
    t = t//10
print("Chu so lon nhat cua so nguyen duong n la: ", lc)
