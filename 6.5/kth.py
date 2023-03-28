from random import randint
def partition(a, l, r, pivot_i):
    pivot = a[pivot_i]
    i = j = l
    a[pivot_i], a[i] = a[i], a[pivot_i]
    i += 1
    while(j <= r):
        if a[j] > pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
        j += 1
    i -= 1
    a[i], a[l] = a[l], a[i]
    return i
def kth(a, l, r, k):
    if r - l  == 0: 
        return a[l]
    pivot = randint(l, r)
    p = partition(a, l, r, pivot)
    if p + 1 == k:
        return a[p]
    elif p + 1 > k:
        return kth(a, l, p , k)
    else:
        return kth(a, p + 1, r, k)
l = [3,2,3,1,2,4,5,5,6]
print(kth(l, 0, len(l) - 1, 8))