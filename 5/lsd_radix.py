def counting_sort(a, digit):
    tmp = [0]*28
    res = [0] * len(a)
    for word in a:
        tmp[ord(word[digit]) - 97] += 1
    #теперь каждый элемент tmp будет хранить количество эл-тов
    #меньше или равных себе
    for i in range(1, 28):
        tmp[i] = tmp[i] + tmp[i - 1]
    #тем что мы идем с конца массива обеспечивается стабильность сортировки
    for i in range(len(a) - 1, -1, -1):
        res[tmp[ord(a[i][digit]) - 97] - 1] = a[i]
        tmp[ord(a[i][digit]) - 97] -= 1
    return res

def lsd_radix_sort(a):
    res = a.copy()
    dg = len(a[0])
    for i in range(dg - 1, -1, -1):
        res = counting_sort(res, i)
    return res
a = ['afbd', 'sdfa', 'aaaa', 'bbdk']
b = lsd_radix_sort(a)
print(b)