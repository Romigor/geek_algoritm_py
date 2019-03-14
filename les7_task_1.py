
# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный 
# массив, заданный случайными числами на промежутке [-100; 100). 
# Выведите на экран исходный и отсортированный массивы. Сортировка должна быть 
# реализована в виде функции. 
# По возможности доработайте алгоритм (сделайте его умнее).

import random

SIZE = 10
MAX_LIMIT = 99
MIN_LIMIT = -100
array = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]

sort_array = array.copy() 
sort_array_smart = array.copy() 

def babls_sort(x):
    n = 1
    while n < len(x):
        for i in range(len(x) - n):
            if x[i] > x[i + 1]:
                x[i], x[i + 1] = x[i + 1], x[i]
        n += 1      

def babls_sort_smart(x):
    n = 1
    while n < len(x):
        cnt_permutation = 0 
        for i in range(len(x) - n):
            if x[i] > x[i + 1]:
                x[i], x[i + 1] = x[i + 1], x[i]  
                cnt_permutation += 1  
        
        print(cnt_permutation)
        if cnt_permutation == 0:
            break
        n += 1
        
babls_sort(sort_array)
babls_sort_smart(sort_array_smart)

print(array)
print(sort_array)
print(sort_array_smart)
