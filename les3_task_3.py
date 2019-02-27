# В массиве случайных целых чисел поменять местами минимальный и максимальный 
# элементы.

import random

SIZE = 10
MAX_LIMIT = 100
MIN_LIMIT = 0
array = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]


pos_max = 0
pos_min = 0
num_max = MIN_LIMIT
num_min = MAX_LIMIT 

print(array)
 
for i,item in enumerate(array):
    if item > num_max:
        num_max = item
        pos_max = i
        
    if item < num_min:
        num_min = item
        pos_min = i    
        
array[pos_max] = num_min   
array[pos_min] = num_max     

print(array)

 