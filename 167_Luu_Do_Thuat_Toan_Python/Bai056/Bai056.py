
n = float(input("Nhap n: "))
s = 0
i = 1

while(i <= n ):
    if (n%i==0):
        if (i%2==0):
            s = s+i     
    i = i+1

print ("Tong cac uoc so chan cua n: ", s)
