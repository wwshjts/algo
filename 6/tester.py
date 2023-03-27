import os
from random import randint
from format_tb import format_table
l = 1000000
a = [(randint(1,2000)) for _ in range(l)]
test_case = sorted(a)
with open('input.txt', 'w') as f:
    f.write(str(l) + '\n')
    for x in a:
        f.write(str(x) + ' ')
    
os.system('./a.out')
with open('output.txt', 'r') as f:
    for i in range(3):
        tmp = list(map(int, f.readline().strip().split(' ')))
        if tmp != test_case:
            print("ALARM")
        print(f.readline())

#with open('output.txt', 'r') as f:
#    res =[]
#    for i in range(3):
#        res.append(float(f.readline())) 
#    print(res)
#    format_table(['1'], ['hoare', 'lomuto_naive', ], [res])