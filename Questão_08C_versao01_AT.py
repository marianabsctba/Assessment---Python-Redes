import multiprocessing, time, random


def lin():
    print("==" * 30)


def print_time():
    lin()
    print(f"=== EXECUÇÃO MULTIPROCESSO : {N} ===")
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


def calc_fact(lis, Q):
    for i in lis:
        fat = factorial(i)
        B.append(fat)
    Q.put(B)


A = []

B = []

if __name__ == "__main__":
    
    N = 50000

    P = []

    init_q = 0
    
    c = 1
    
    num_process = 4
    
    q_end = multiprocessing.Queue()

    start = float(time.time())

    for i in range(N):
        A.append(random.randint(1, 10))

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
    
    print_time()
        
