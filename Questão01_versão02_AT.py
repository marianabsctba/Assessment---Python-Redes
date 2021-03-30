import psutil

def lin():
    print('==' * 40)
    

def print_infos():
    print("{:<6} {:<20.19} {:>10} {:>6}".format('PID', 'NOME', 'MEMÓRIA (%)', 'CPU (%)'))
    
def info_process(): 
    for process in psutil.process_iter():
        try:
            info = process.as_dict(attrs=['name', 'pid', 'memory_percent', 'cpu_percent']) #versão utilizando dict
            info['memory_percent'] = round(process.memory_percent(), 2)
            info['cpu_percent'] = round(process.cpu_percent(interval=1), 2) #incluído intervalo para não zerar % de CPU

            text = '{:<6}'.format(info['pid'])
            text = text + '{:<20.19}'.format(info['name'])
            text = text + '{:>10.2f}'.format(info['memory_percent'])
            text = text + '{:>10.2f}'.format(info['cpu_percent'])
            
            lin()
            print_infos()
            lin()
            print(text)

        except psutil.NoSuchProcess:
            pass
        
info_process()
