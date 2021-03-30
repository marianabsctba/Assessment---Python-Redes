#Questão 06)
#Escreva um programa cliente e servidor sobre TCP em Python em que:
#O cliente envia para o servidor o nome de um diretório e recebe a lista de arquivos (apenas arquivos) existente nele.
#O servidor recebe a requisição do cliente, captura o nome dos arquivos no diretório em questão e envia a resposta ao cliente de volta.

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
    
    for j in lista:
        print('{:<10}'.format(j), end=' ')
        

#socket cliente
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#tempo (segundos)
socket_cliente.settimeout(5)
destino = (socket.gethostname(), 9999)
msg = ''
print("Cliente enviando requerimento ao servidor...")
socket_cliente.sendto(msg.encode('utf8'), destino)

try:
    for i in range(5):
        recv_msg()
        break
except socket.timeout as error:
    print(str(error))

input('\nClique em qualquer tecla para sair..')
