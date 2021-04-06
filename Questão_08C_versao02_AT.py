from multiprocessing import Pool #utilizado o Pool do multiprocessing
from random import randint
import time


N = 50000

def factorial(n):
    factorial = n
    for i in range(n - 1, 1, -1):
        factorial = factorial * i
    return (factorial)
    

if __name__ == "__main__":
    
    start = float(time.time())

    with Pool(processes=4) as pool: #4 processos
        A = []
        for i in range(N):
            A.append(randint(1, 10))

        B = []
        for i in A:
            B.append(factorial(i))

    end = float(time.time())
    
    elapsed = end - start

    print('Início:',start)
    print('Fim:', end)
    print('Tempo total:', round(elapsed, 2),'segundos.')
