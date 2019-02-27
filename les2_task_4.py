#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input('Введите натурльное число: '))
element = -2
result = 0

for i in range(n):
    element /= -2 
    result += element

print(f'Сумма ряда = {result}')