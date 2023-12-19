import socket
import threading
import datetime

def getTime():
    now = datetime.datetime.now()
    hour = str(now.hour)
    minute = str(now.minute)
    second = str(now.second)
    if len(hour) < 2:
        hour = '0'+hour
    elif len(minute) < 2:
        minute = '0'+minute
    elif len(second) < 2:
        second = '0'+second
    return hour+':'+minute+':'+second

def conexao_socket(serverSocket):
    while (True):
        data, address = serverSocket.recvfrom(2048)
        '''
        PROTOCOLO
        '''
        mensagem = data.decode()
        if (mensagem == '0'):
            serverSocket.sendto('0'.encode(), address)
            break
        elif (mensagem == '1'):
            serverSocket.sendto(getTime().encode(), address)
            break
        else:
            serverSocket.sendto('Opção inválida'.encode(), address)
            break


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('localhost', 20001)
print("Iniciando servidor na porta %s %s" % server_address)
#Reservando porta
sock.bind(server_address)
#Escutando na porta reservada

#Iniciando protocolo

while True:
    conexao = threading.Thread(target=conexao_socket,args=(sock,))
    conexao.start()



