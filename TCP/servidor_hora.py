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

def conexao_cliente(client,address):
    
    while (True):
        data = client.recv(2048)
        '''
        PROTOCOLO
        '''
        mensagem = data.decode()
        if (mensagem == '0'):
            client.send('0'.encode())
            break
        elif (mensagem == '1'):
            client.send(getTime().encode())
        else:
             client.send('Opção inválida'.encode())

    #Fechando o socket
    client.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('localhost', 20001)
print("Iniciando servidor na porta %s %s" % server_address)
#Reservando porta
sock.bind(server_address)
#Escutando na porta reservada
sock.listen(1)

#Iniciando protocolo

while True:
    client, address = sock.accept()
    conexao = threading.Thread(target=conexao_cliente,args=(client,address,))
    conexao.start()



