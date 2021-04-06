from random import randint
import time

N = 50000

A = []
B = []

def lin():
    print("==" * 30)


def print_time():
    lin()
    print("== EXECUÇÃO SEQUENCIAL ==")
    lin()
    print('Tempo inicial: ', start, 'segundos.')
    print('Tempo final: ', end, 'segundos.')
    print('Tempo total: ', elapsed, 'segundos.')
    lin()
    
    
def factorial(n):
    factorial = n
    for i in range(n - 1, 1, -1):
        factorial = factorial * i
    return (factorial)


start = float(time.time())

for i in range(N):
    A.append(randint(1, 10))

for i in A:
    B.append(factorial(i))

end = float(time.time())

elapsed = end - start


print_time()


