#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def last_to_first(x):
    
    last_num = str(int(x) % 10)
    other_num = str(int(x) // 10)
    
    if other_num == '0':
        return last_num
    else:
        return last_num + last_to_first(other_num)
    
    
num = input('Введите натурльное число: ')

print(f'Обратное число: {int(last_to_first(num))}')  
