import socket
import threading

def receber_mensagens(sock):
    while (True):
        data = sock.recv(2048)
        mensagem = data.decode()
        if mensagem!='0':
            #Imprimindo a mensagem recebida
            print(data.decode())
        else:
            print('Fechando conexão')
            sock.close()
            break

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
server_address = ('localhost', 20001)
print ("Conectando %s porta %s" % server_address)
#Conectando ao servidor
sock.connect(server_address)
recepcao = threading.Thread(target=receber_mensagens,args=(sock,))
recepcao.start()
while (True):    
    print("Digite o número correspondente as opções abaixo")
    message = input("[1] Hora atual\n[0] Fechar\n")
    #Enviando mensagem ao servidor
    sock.send(message.encode('utf-8'))
    if message == '0':
        break

recepcao.join()