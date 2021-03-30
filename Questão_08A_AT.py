from random import randint
import time

N = 50000

def factorial(n):
    factorial = n
    for i in range(n - 1, 1, -1):
        factorial = factorial * i
    return (factorial)


def time_execution():
    start = float(time.time())

    A = []
    for i in range(N):
        A.append(randint(1, 10))

    B = []
    for i in A:
        B.append(factorial(i))

    #tempo final
    end = float(time.time())    
    elapsed = end - start

    print('Tempo inicial: ', start)
    print('Tempo final: ', end)
    print('Tempo total sequencial: ', round(elapsed, 2), 'segundos.')
    

time_execution()
