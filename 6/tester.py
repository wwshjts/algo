import os
from random import randint
from format_tb import format_table
l = 100000
a = [(randint(1,10)) for _ in range(l)]
with open('input.txt', 'w') as f:
    f.write(str(l) + '\n')
    for x in a:
        f.write(str(x) + ' ')
    
os.system('./a.out')
with open('output.txt', 'r') as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())
#with open('output.txt', 'r') as f:
#    res =[]
#    for i in range(3):
#        res.append(float(f.readline())) 
#    print(res)
#    format_table(['1'], ['hoare', 'lomuto_naive', ], [res])