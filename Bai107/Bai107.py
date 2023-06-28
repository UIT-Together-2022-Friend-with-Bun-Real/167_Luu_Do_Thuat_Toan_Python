from importlib import machinery
import math
from platform import machine
from re import I, M
from tkinter import N
x = float(input("Nhap x: "))
xx = (x * 3.14) / 180
s = 1
t = 1
m = 1
dau = -1
e = 1
i = 2
while e > 0.000001:
    t = t * xx * xx
    m = m * (i - 1)*i
    e = t / m
    s = s + dau*e
    dau = - dau
    i = i + 2
print("Ket qua: ", s)

