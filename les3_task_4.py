# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MAX_LIMIT = 5
MIN_LIMIT = 0
array = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]

print(array)

uniq_num_array =[]
count_ = []

for item in array:
    if item not in uniq_num_array:
        uniq_num_array.append(item)
        count_.append(1)
    else:
        count_[uniq_num_array.index(item)] += 1
               
pos_max = 0
num_max = 0
        
for i, item in enumerate(count_):
     if item > num_max:
        num_max = item
        pos_max = i 
    
print(uniq_num_array)
print(count_)
print(f'Чаще всего в массиве встречается цифра: {uniq_num_array[pos_max]}')

        
        