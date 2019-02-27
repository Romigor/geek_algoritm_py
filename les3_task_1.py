# В диапазоне натуральных чисел от 2 до 99 определить, 
# сколько из них кратны любому из чисел в диапазоне от 2 до 9.

number = [x for x in range(2,9)]
array = [x for x in range(2,99)]


for item in number:
    count_ = 0 
    for i in array:
        if i % item == 0: 
            count_ += 1 
    
    print(f'{item} - {count_}')    
 
