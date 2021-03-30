#Questão 08 (A)

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
    t_init = float(time.time())

    for i in A:
        fatorial(i)
        
    t_end = float(time.time())

    #print(A)
    #print(B)
    print('Início:',t_init)
    print('Fim:',t_end)
    tt = t_end - t_init
    print('Tempo total sequencial:', round(tt,2),'segundos.')
    
    
create_list(n)
execution_time()
