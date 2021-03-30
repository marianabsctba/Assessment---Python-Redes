#Questão 1)
#Escreva um programa em Python que:
    #A - obtenha a lista de processes executando no momento, considerando que o processo pode deixar de
    #existir enquanto seu programa manipula suas informações;
    #B - imprima o nome do processo e seu PID;
    #C - imprima também o percentual de uso de CPU e de uso de memória.
    

import psutil, sys


def memory_percent():
    return round(pid.memory_percent(), 2)


def cpu_percent():
    return int(pid.cpu_percent(interval=1))

try:
    processes = psutil.pids()
    
    for process in processes:      
        pid = psutil.Process(process)
        name = pid.name()                
        memo = memory_percent()
        c = cpu_percent()
        
        print("Nome: {:<20} Pid: {:<10} Memória: {:>5}% CPU: {:>5}%".format(name, process, memo, c))

except Exception as NoSuchProcess:
    print(NoSuchProcess)
   
