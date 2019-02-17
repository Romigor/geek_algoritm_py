# -*- coding: utf-8 -*-

print("Введите порядковый номер буквы")
n = int(input('номер буквы: '))

s = chr(ord('a') - 1 + n )
print(f"Буква: {s}")