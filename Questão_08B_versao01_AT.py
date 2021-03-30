import threading, time
from random import randint  #realizando o cálculo comum das threadings

N = 50000


A = []
B = []
T = []

threads = 4

def factorial(n):
    factorial = n
    for i in range(n - 1, 1, -1):
        factorial = factorial * i
    return (factorial)


def calc_fact(lis, start_t, end_t):
    for i in range(start_t, end_t):
        B.append(factorial(lis[i]))


def time_execution():
    start = float(time.time())
    
    for i in range(N):
        A.append(randint(1, 10))
     
    for i in range(threads):
        start_t = i * int(N/threads)
        end_t = (i + 1) * int(N/threads)
        th = threading.Thread(target=calc_fact, args=(A, start_t, end_t))
        th.start()
        T.append(th)
    
    for th in T:
        th.join()
        
    end = float(time.time())    
    elapsed = end - start

    print('Tempo inicial: ', start)
    print('Tempo final: ', end)
    print('Tempo total paralelo (4 threads): ', round(elapsed, 2), 'segundos.')
    
time_execution()
