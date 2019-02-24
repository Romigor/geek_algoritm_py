#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def row_print(start_simbol, num_simbol = 10):
    n = 0
    one_row = ''

    while n < num_simbol:
       one_row = one_row + ' ' + str(start_simbol+n) + '-' + chr(start_simbol+n) 
       n += 1    
    
    return print(one_row)           
           

start = 32 
end = 127
int_iter = (end-start +1) // 10

for i in range(int_iter):
    row_print(start + i*10 )

row_print(int_iter*10 + start, 1 + end - (int_iter*10 + start) )
     
     