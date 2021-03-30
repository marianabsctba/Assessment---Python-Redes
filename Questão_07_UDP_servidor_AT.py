import socket, psutil, pickle
from psutil._common import bytes2human

def mem():    
    resp_list = []
    
    mem = psutil.virtual_memory()
    mt = bytes2human(mem.total)
    mf = bytes2human(mem.free)
    
    resp_list.append(mt)
    resp_list.append(mf)
    
    return resp_list
    


socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
HOST = socket.gethostname()
PORT = 9999
socket_servidor.bind((HOST, PORT))
print('Servidor', HOST, 'esperando conexão na porta', PORT, '...')


while True:
    (msg, client) = socket_servidor.recvfrom(1024)
    print("Requerimento recebido do cliente...")
    data = pickle.dumps(mem())
    socket_servidor.sendto(data, client)
    print("Enviando dados de memória para cliente...")

socket_servidor.close()
