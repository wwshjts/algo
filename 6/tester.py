import os
from random import randint
l = 10

with open('input.txt', 'w') as f:
    f.write(str(l) + '\n')
    for _ in range(l):
        f.write(str(randint(1, 9)) + ' ')
    
os.system('./a.out')

with open('output.txt', 'r') as f:
    print(f.readline())
