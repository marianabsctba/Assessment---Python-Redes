#Questão 08 (C)

from multiprocessing import Pool
import time, random

n = int(input("Digite o tamanho do vetor: "))


A = []

B = []


def create_list(n):
    for i in range(n):
        c = random.randint(1,10)
        A.append(c)
    return A

def fatorial(n):
    fat = n
    for i in range(n-1,1,-1):
        fat = fat * i
        B.append(fat)
    return B


def execution_time():   
    for i in A:
        fatorial(i)      


def main():
    t_init = float(time.time())
    
    with Pool(processes=4) as pool: #4 processos
        e = execution_time()

    t_end = float(time.time())
    
    print('Início:',t_init)
    print('Fim:',t_end)
    tt = t_end - t_init
    print('Tempo total:', round(tt,2),'segundos.')



if __name__ == "__main__":
    main()
