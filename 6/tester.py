import os
from random import randint
from 9.py import format_table
l = 10
a = [(randint(1,9)) for _ in range(l)]
with open('input.txt', 'w') as f:
    f.write(str(l) + '\n')
    for x in a:
        f.write(str(x) + ' ')
    
os.system('./a.out')
print(a)
with open('output.txt', 'r') as f:
    print(f.readline())
