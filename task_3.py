# -*- coding: utf-8 -*-

print("Введите координаты первой точки")
X1 = float(input('X1: '))
Y1 = float(input('Y1: '))

print("Введите координаты первой точки")
X2 = float(input('X2: '))
Y2 = float(input('Y2: '))

k = (Y2-Y1)/(X1-X2)
b = Y2 - k*X2

print(f'Уранение прямой: y = {b:.2f} + {k:.2f}*x ')