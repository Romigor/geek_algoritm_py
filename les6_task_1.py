# Определить, какое число в массиве встречается чаще всего.

# Определим функцию которая считает полный размер элемента                
import sys

def get_size(x, size = 0):
    size += sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                size = get_size(key, size )
                size = get_size(value, size)
        elif not isinstance(x, str):        
            for item in x:
                size = get_size(item, size) 
    return(size)    

# Оригинальное решние
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


# Объем памяти
sum([ get_size(SIZE)
    ,get_size(MAX_LIMIT)
    ,get_size(MIN_LIMIT)
    ,get_size(array)
    ,get_size(uniq_num_array)
    ,get_size(count_)
    ,get_size(item)
    ,get_size(pos_max)
    ,get_size(num_max)
    ,get_size(i)] 
) # результат 1248

        
# Вариант 2 ###################################################################
import collections as col

params = col.namedtuple('params','SIZE, MAX_LIMIT, MIN_LIMIT')
params = params(SIZE = 10, MAX_LIMIT = 5, MIN_LIMIT = 0)

array = [random.randint(params.MIN_LIMIT, params.MAX_LIMIT) for _ in range(params.SIZE)]

cnt_uniq_num = col.Counter()

for item in array:
    cnt_uniq_num[item] += 1

print(cnt_uniq_num)
print(f'Чаще всего в массиве встречается цифра: {cnt_uniq_num.most_common(1)[0][0]}') 

# Объем памяти
sum([ get_size(params)
    , get_size(array)
    , get_size(cnt_uniq_num)
    , get_size(item)
    ]) # результат 1364

# Вариант 3 ###################################################################

SIZE = 10
MAX_LIMIT = 5
MIN_LIMIT = 0
MAX_NUM = 0 

tp = tuple(random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE))

for item in set(tp):
    if tp.count(item) > tp.count(MAX_NUM):
        MAX_NUM = item

print(tp)
print(f"Чаще всего в массиве встречается цифра: {params['MAX_NUM']}") 

# Объем памяти
sum([ get_size(SIZE)
     ,get_size(MAX_LIMIT)
     ,get_size(MIN_LIMIT)
     ,get_size(MAX_NUM)
     ,get_size(set(tp))
     ,get_size(tp)
     ,get_size(item)
     ]) # результат 1408