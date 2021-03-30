import multiprocessing, time, random

#usando maneira mais longa de cálculo

N = 50000

A = []

B = []

P = []

def factorial(n):
    factorial = n
    for i in range(n - 1, 1, -1):
        factorial = factorial * i
    return (factorial)


def calc_fact(lis, Q):
    for i in lis:
        fat = factorial(i)
        B.append(fat)
    Q.put(B)



def multiprocess():
    start = float(time.time())
    
    for i in range(N):
        A.append(random.randint(1, 10))
    
    init_q = 0
    c = 1
    num_process = 4
    q_end = multiprocessing.Queue()
    
    for i in range(num_process):
        end_q = int((N // num_process) * c)
        p = multiprocessing.Process(target=calc_fact, args=(A[init_q:end_q], q_end))
        p.start()
        P.append(p)
        init_q = end_q
        c += 1
        
    while q_end.empty is False:
        for process in P:
            process.join()
            
    for i in range(0, num_process):
        for i in q_end.get():
            B.append(i)
    
    end = float(time.time())
    elapsed = end - start
        
    print('Início:',start)
    print('Fim:', end)
    print('Tempo total:', round(elapsed, 2),'segundos.')

if __name__ == "__main__":
    multiprocess()
