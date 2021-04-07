import socket, pickle

def lin():
    print('==' * 20)
    

#receber mensagem
    
def recv_msg():
    bytes = socket_cliente.recv(1024)
    lista = pickle.loads(bytes)
    
    print("Dados recebidos do servidor....")
    lin()
    print('Informações de memória:')
    lin()
    print('{:<10}'.format('Total') + '{:<10}'.format('Livre (disponível)'))
    lin()
    
    for i in lista:
        print('{:<10}'.format(i), end=' ')
        

#socket cliente
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

destino = (socket.gethostname(), 9999)

socket_cliente.settimeout(5)

try:
    msg = ''
    print("Cliente enviando requerimento ao servidor...")
    socket_cliente.sendto(msg.encode('utf8'), destino)
    recv_msg()
except:
    print("Cliente não conseguiu receber os dados... Tentando novamente")
    try:
        for i in range(5):
            recv_msg()
    except socket.timeout as error:
        print(str(error))
finally:
    socket_cliente.close()
