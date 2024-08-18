# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
distance = float(input("Ban hay nhap diem trung binh (GPA) cua ban:"))
if distance < 3.5:
    print("Hoc luc Kem")
elif distance >= 3.5 and distance < 5.0:
    print("Hoc luc Yeu")
elif distance >= 5.0 and distance < 7.0:
    print("Hoc luc Trung Binh")
elif distance >= 7.0 and distance < 8.0:
    print("Hoc luc Kha")
elif distance >= 8.0 and distance < 9.0:
    print("Hoc luc Gioi")
elif distance >= 9.0 and distance < 10:
    print("Hoc luc Xuat sac")
else:
    print("Khong xac dinh")
    