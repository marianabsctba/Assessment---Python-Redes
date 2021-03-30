#Questão 08 (B)

from random import randint
import time, concurrent.futures #usei o Threading Pool

N = 50000

def factorial(n):
    factorial = n
    for i in range(n - 1, 1, -1):
        factorial = factorial * i
    return (factorial)

#tempo inicial


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
    print('Tempo total com 4 threads: ', round(elapsed, 2), 'segundos.')    


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor: #4 threads
        executor.map(time_execution())

