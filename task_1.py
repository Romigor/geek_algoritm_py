# -*- coding: utf-8 -*-

print('Введите трёхзначное число: ')
k = int(input('k = '))

f = k % 10
s = k // 10 % 10
t = k // 100

sm = f+s+t
prod = f*s*t

print(f'sum = {sm} , multiply = {prod}') 

