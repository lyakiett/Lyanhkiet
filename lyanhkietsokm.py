# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 10:22:40 2024

@author: Student
"""

print("nhap so km quang duong di duoc cua ban:")
km=float(input("so km cua ban:"))
if km <= 1:
    thanhtoan=20
    print("So tien ban thanh toan la 20k", thanhtoan)
elif km <= 3:
    thanhtoan=km*13
    print("So tien ban phai thanh toan la")
    print("thanh toan=", thanhtoan)
elif km <= 8:
    thanhtoan=km*12
    print("So tien ban phai thanh toan la")
    print("thanh toan=", thanhtoan)
elif km <= 100:
    thanhtoan=km*10
    print("So tien ban phai thanh toan la")
    print("thanh toan=", thanhtoan)
else:
    thanhtoan=(km*10)-((km*10)/100)*8
    print("So tien ban phai thanh toan la")
    print("thanh toan=", thanhtoan)