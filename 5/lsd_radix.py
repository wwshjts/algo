from random import randint
a_code = 97
alphas = 25
def test_sort(algh):
    a = ['wwww', 'oooo', 'wwww']
    print(f'testing {algh.__name__}')
    print(f'test case 1: {"correct" if sorted(a) == algh(a) else "false"}')
    for i in range(1, 10 + 1):
        a = [''.join([chr(x + a_code) for x in range(1, alphas)]) for _ in range(10)]
        print(f'test case {i + 1}: {"correct" if sorted(a) == algh(a) else "false"}')
def counting_sort(a, digit):
    tmp = [0]*alphas
    res = [0] * len(a)
    for word in a:
        tmp[ord(word[digit]) - a_code] += 1
    #теперь каждый элемент tmp будет хранить количество эл-тов
    #меньше или равных себе
    for i in range(1, alphas):
        tmp[i] = tmp[i] + tmp[i - 1]
    #тем что мы идем с конца массива обеспечивается стабильность сортировки
    for i in range(len(a) - 1, -1, -1):
        res[tmp[ord(a[i][digit]) - a_code] - 1] = a[i]
        tmp[ord(a[i][digit]) - a_code] -= 1
    return res

def lsd_radix_sort(a):
    '''lsd_radix_sort'''
    res = a.copy()
    dg = len(a[0])
    for i in range(dg - 1, -1, -1):
        res = counting_sort(res, i)
    return res
test_sort(lsd_radix_sort)