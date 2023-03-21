from random import randint 
def count_digits(a):
    cnt = 0
    while a > 0:
        cnt += 1
        a = a // 10
    return cnt

def karatsuba(x, y):
    """Умножение Карацубы"""
    if (x < 10) or (y < 10):
        return x * y
    n = max(count_digits(x), count_digits(y))
    mid = n // 2 
    a = x // 10**(mid)
    b = x % 10 **(mid)
    c = y // 10**(mid)
    d = y % 10 **(mid)
    i = karatsuba(a, c)
    k = karatsuba(b,d)
    j = karatsuba(a + b, c + d) - i - k
    return i * 10**(mid * 2)  + j * 10**(mid) + k

def test(mult):
    print("Тестируем ", mult.__doc__)
    for i in range(1, 2):
        a = randint(10e4, 10e9)
        b = randint(10e4, 10e9)
        res = karatsuba(a,b) 
        if karatsuba(a,b) == (a*b):
            print(f"testcase{i}: ok")
        else: print(f'testcase{i}: fail: {res} != {a*b} ')
    a = 10**9
    b = 1
    res = karatsuba(a,b) 
    if karatsuba(a,b) == (a*b):
        print(f"testcase{11}: ok")
    else: print(f'testcase{11}: fail: {res} != {a*b} ')
test(karatsuba)