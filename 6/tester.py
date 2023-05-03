#!/usr/bin/python
import os
from random import randint
from format_tb import format_table
l = 1000000
n = 5
names = ['hoare', 'naive', 'giga']
os.system('clang -Ofast sort_hoare.c -o hoare')
os.system('clang -Ofast sort_lomuto_naive.c -o naive')
os.system('gcc -Ofast -DNEBUG sort_giga_lomuto.cpp -o giga')
#Избавиться от повторений во воходе
for i in range(1, 5):
    a = [(randint(1,200000)) for _ in range(l)]
    test_case = sorted(a)
    with open('input.txt', 'w') as f:
        f.write(str(l) + '\n')
        for x in a:
            f.write(str(x) + ' ')
    res = []
    for i in range(3):
        os.system('./' + names[i])
        with open('output.txt', 'r') as f:
            res.append(float(f.readline())) 
            tmp = list(map(int, f.readline().strip().split(' ')))
            if tmp != test_case:
                print("ALARM")
    print(res)

os.system(f'rm {names[0]} {names[1]} {names[2]}')