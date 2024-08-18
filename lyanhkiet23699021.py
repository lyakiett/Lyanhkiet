# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:50:44 2024

@author: Student
"""

import math
print("ax^2+bx+c")
a=float(input("Nhap a:"))
b=float(input("Nhap b:"))
c=float(input("Nhap c:"))
denta=float()
denta=b*b-4*a*c
if denta < 0:
    print("Phuong trinh vo nghiem")
elif denta == 0:
    x= (-b/(2*a))
    print("x la nghiem kep x la:", x)
else:
    x1= (-(b)+math.sqrt(denta))/(2*a)
    x2= (-(b)-math.sqrt(denta))/(2*a)
    print("Phuong trinh co hai nghiem:")
    print("x1=", x1)
    print("x2=", x2)

