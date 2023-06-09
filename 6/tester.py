#!/usr/bin/python
import os
from random import randint, shuffle
from format_tb import format_table
l = 400000 
n = 5
names = ['hoare', 'naive', 'giga']
os.system('gcc -Ofast sort_hoare.c -o hoare')
os.system('gcc -Ofast sort_lomuto_naive.c -o naive')
os.system('gcc -Ofast sort_giga_lomuto.cpp -o giga')
for i in range(1, n):
    a = [i for i in range(1,l + 1)]
    shuffle(a)
    test_case = sorted(a)
    with open('input.txt', 'w') as f:
        f.write(str(l) + '\n')
        for x in a:
            f.write(str(x) + ' ')
    res = []
    for name in names:
        os.system('./' + name)
        with open('output.txt', 'r') as f:
            res.append(float(f.readline())) 
            tmp = list(map(int, f.readline().strip().split(' ')))
            for i in range(len(test_case)):
                if test_case[i] != tmp[i]:
                    print(f'alg {name} ')
                    print(f'ERROR {test_case[i]} != {tmp[i]}')
                    break

    print(res)

os.system(f'rm {names[0]} {names[1]} {names[2]}')