#!/usr/bin/env python3
# -*- coding: utf-8 -*-

num = int(input('Введите натуральное число: '))

length_num = len(str(num))
number_chet_num = 0 
#i = 0

for i in range(length_num):
    
    stock = (num // (10**i) % 10) % 2
    
    if stock == 0:
        number_chet_num += 1
    
 #   i += 1
       
print(f'Кол-во четных цифр = {number_chet_num}\nКол-во нечетных цифр = {length_num -number_chet_num}' )     