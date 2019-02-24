#!/usr/bin/env python3
# -*- coding: utf-8 -*-

operation = input('Choose oparation: ')

while operation != '0':
    
    if  (operation == '+') | (operation == '-') | (operation == '*') | (operation == '/'):
    
        first_num  = int(input('Введите первое число: '))
        second_num = int(input('Введите второе число: '))
        
        if operation == '+':
            result = first_num + second_num
            print(result)
            
        elif operation == '-':
            result = first_num - second_num
            print(result)
        
        elif operation == '*':
            result = first_num * second_num
            print(result)
        
        else: 
            
            if second_num !=0:
                result = first_num / second_num
                print(result)
            else:
                print('Делить на 0 нельзя')
             
    else:
        print('Выбрана недоступная операция')
    
    
    operation = input('Choose oparation: ')
    
    
    
  