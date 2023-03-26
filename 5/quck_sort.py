
from  random import randint
nums = [randint(1, 10) for _ in range(5)]
nums = [3, -1]
n = len(nums)

def partition(a, l, r):
    pivot_1 = randint(l + 1, r)
    pivot_2 = randint(l, pivot_1 - 1)
    pivot_i = pivot_1 if a[pivot_1] <= a[pivot_2] else pivot_2
    pivot = a[pivot_i]
    a[l], a[pivot_i] = a[pivot_i], a[l]
    pivot_i = l
    l  += 1
    while l <= r:
        while a[l] < pivot:
            l += 1
        while a[r] > pivot:
            r -= 1
        if l >= r:
            break
        a[l], a[r] = a[r], a[l]
        r -= 1
        l += 1
    if a[l] > pivot:
        l -= 1
    a[l], a[pivot_i] =  a[pivot_i], a[l]
    return l
    

def sort(a, l, r):
    if r - l < 1:
        return
    p = partition(a, l, r)
    sort(a, l, p - 1)
    sort(a, p + 1, r)

print(nums)
sort(nums, 0, n - 1)
print(nums)