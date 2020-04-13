'''
Fibonacci sequence w/ recursion and memioze solution
'''

import time

def fib(n):
    #a = 1
    b = 1
    c = 2
    if n <= 0:
        return -1
    elif n == 1 or n == 2:
        return 1
    elif n == 3:
        return c
    else:
        for _ in range(n - 3):
            temp = 0
            temp = b + c
            b = c
            c = temp
            #a = b
    return c

def fib_recurs(n):
    if n <= 0:
        return -1
    elif n == 1 or n == 2:
        return 1
    else:
        return fib_recurs(n-1) + fib_recurs(n-2)

def fib_recurs_mem(n, memo):
    if memo[n] is not None:
        return memo[n]
    elif n <= 0:
        result = 0
    elif n == 1 or n == 2:
        result =  1
    elif (memo[n-1] is not None) and (memo[n-2] is not None):
        result = memo[n]
    else:
        result = fib_recurs_mem(n-1, memo) + fib_recurs_mem(n-2, memo)
    memo[n] = result
    return result

if __name__ == '__main__':
    size = 50
    fibArr = [1,1,1]

    if fibArr[0] == 1:
        start = time.time()
        print(f'fib({size}) = ',fib(size))
        end = time.time()
        print(f'For loop = {end-start} s')

    if fibArr[1] == 1:
        start = time.time()
        print(f'fib_recurs({size}) = ',fib_recurs(size))
        end = time.time()
        print(f'Recursive = {end-start} s')

    if fibArr[2] == 1:
        arr = [None] * (size+1)
        start = time.time()
        print(f'fib_recurs_mem({size}) = ',fib_recurs_mem(size,arr))
        end = time.time()
        print(f'Recursive Mem = {end-start} s')