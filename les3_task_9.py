# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

M = 10
N = 5
MAX_LIMIT = 9
MIN_LIMIT = 0
matrix = [[random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(M)] for _ in range(N)]

for line in matrix: 
    print(line)
    
min_column = [MAX_LIMIT] * len(matrix[0]) 

for line in matrix:
    for i, item in enumerate(line):
        if item < min_column[i]:
            min_column[i] = item
  
print('\n', min_column) 
        
max_of_min = 0
        
for item in min_column:
     if item > max_of_min:
        max_of_min = item
        
print(f'максимальное из минимальных значений в колонках = {max_of_min}') 
        