# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 10:03:31 2024

@author: Student
"""

print("nhap 3 canh cua tam giac")
a=float(input("Nhap canh a:"))
b=float(input("Nhap canh b:"))
c=float(input("Nhap canh c:"))
if a==b and b==c:
    print("Day la tam giac deu")
elif a==b or a==c or c==b:
    print("Day lam tam giac can")
elif a*a+b*b==c*c:
    print("Day la tam giac vuong")
elif a==0 or b==0 or c==0:
    print("Day khong phai la tam giac")
else:
    print("Day la tam giac thuong")
    