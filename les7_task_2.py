# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
# заданный случайными числами на промежутке [0; 50). 
# Выведите на экран исходный и отсортированный массивы.

import random

array = [random.random()*50 for _ in range(10)]

def merge(left, right):
    
    result = []
    i = 0 
    j = 0
    
    while i < len(left) and j < len(right):
         
        if left[i] < right[j]:
            result.append(left[i])
            i += 1 
        else:
            result.append(right[j])
            j += 1
            
    if i == len(left):
        result.extend(right[j:])
        
    if j == len(right):
        result.extend(left[i:])       
        
    return result   


def merge_sort(array):
    #print(array)
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    
    left  = array[ :middle]
    rigth = array[middle: ]

    left = merge_sort(left)
    rigth = merge_sort(rigth)
    result = merge(left, rigth)
    
    return result


sort_array = merge_sort(array)
print(array)
print(sort_array)
