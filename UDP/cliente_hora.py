import socket
import threading

def receber_mensagens(clientSocket):
    while (True):
        data, address = clientSocket.recvfrom(2048)
        mensagem = data.decode()
        if mensagem != '0':
            #Imprimindo a mensagem recebida
            print(mensagem)
            clientSocket.close()
            break
        else:
            print('Aplicação encerrada')
            clientSocket.close()
            break


while (True):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = ('localhost', 20001)
        print("Digite o número correspondente as opções abaixo")
        message = input("[1] Hora atual\n[0] Fechar\n")
        #Enviando mensagem ao servidor
        sock.sendto(message.encode('utf-8'), server_address)
        sock.settimeout(1)
        recepcao = threading.Thread(target=receber_mensagens,args=(sock,))
        recepcao.start()
        if message == '0':
            recepcao.join()
            break
    except:
        print("Request time out")
