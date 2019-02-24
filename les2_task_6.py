#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

random_num = random.randint(0,100)
n = 0

print('Угадайте загаданное число в интервалe от 0 - 100')

while n < 10:
    var = int(input('Ваш вариант: ')) 
    
    if var == random_num:
        print(f'Верно! я загадал число: {random_num}') 
        break
        
    elif var > random_num:
        print('Моё число меньше!') 
        
    else :
        print('Моё число больше!') 
        
        
    n +=1      
 
if n == 10:    
    print(f'Попытки закончились. Моё число {random_num}')     