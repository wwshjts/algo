
from  random import randint
nums = [randint(1, 10) for _ in range(10)]

n = len(nums)

def partition(a, l, r):
    pivot_i = randint(l, r)
    pivot = a[pivot_i]
    while l <= r:
        while a[l] < pivot:
            l += 1
        while a[r] > pivot:
            r -= 1
        if l >= r:
            break
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1
    return r
    

def sort(a, l, r):
    if l >= r:
        return
    p = partition(a, l, r)
    sort(a, l, p)
    sort(a, p + 1, r)

sort(nums, 0, n - 1)