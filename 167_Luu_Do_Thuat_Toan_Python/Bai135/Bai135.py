
year = int(input("Nhap nam can kiem tra : "))
if ((year%4==0 & year%100!=0) | year%400==0):
        print("Nam ", year, " la nam nhuan")
else: print("Nam ", year, " khong la nam nhuan")