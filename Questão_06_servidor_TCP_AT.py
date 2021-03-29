import os, pickle, socket
    

def get_files(dir):
    if os.path.exists(dir):
        list_files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir,f))]        
        return list_files  
    
    else:
        return f'O diretório {dir} não existe. Tente novamente.'
    
    
def server():    
    # socket servidor    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host, port = (socket.gethostname(), 9999)

    s.bind((host, port))
    s.listen()
    
    print(f"Servidor {host} escutando na porta {port}...")
    (socket_cliente, addr) = s.accept()
    
    print(f"Servidor {host} conectado a:", str(addr))

    # recebe pedido do cliente:
    msg_recv = socket_cliente.recv(1024)  
    client_msg = msg_recv.decode('ascii')

    # envia arquivos ao cliente
    data = pickle.dumps(get_files(client_msg))
    print("Enviando dados com tamanho {}...".format(len(data)))
    socket_cliente.send(data)

    print("Os dados foram enviados ao cliente...")
    socket_cliente.close()
    

if __name__ == '__main__':
    server()

