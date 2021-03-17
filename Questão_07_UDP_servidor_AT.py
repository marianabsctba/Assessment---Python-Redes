#server

import pickle
import psutil
import socket


def toGB(v):
    return round(v / 1073741824, 2)


def Avalaible():
    return toGB(psutil.disk_usage(path='C:').free)

def Total():
    return toGB(psutil.disk_usage(path='C:').total)

resposta = ""
try:
    udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (socket.gethostname(), 9991)
    udpServer.bind(dest)

    for i in range(0, 5):
        (msg, host) = udpServer.recvfrom(1024)
        print(msg.decode())
        resposta = '{:>8}'.format(str(Avalaible())) + '{:>8}'.format(str(Total())) + "\n"
        bytes_resp = pickle.dumps(resposta)
        udpServer.sendto(bytes_resp, host)

except Exception as error:
    print(error)

udpServer.close()
