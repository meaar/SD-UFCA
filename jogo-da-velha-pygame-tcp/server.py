import socket
import threading

clients = []

controller = {
    "status" : "waiting"
}

def listener(client, address):
    print ("Accepted connection from: ", address)
    clients.append(client)
    if len(clients) > 2:
        print("CAIU")
        clients.pop()
        client.close()
        return
    while True:

        data = client.recv(1024)
        if data:
            i = 1
            msg = data.decode()

            if msg != 'waiting':
                print(msg)
            for c in clients:
                if msg == 'LOCALPLAYER':
                    newData = 'LOCALPLAYER'+str(i)
                    c.send(newData.encode())
                    i += 1
                else:
                    c.send(data)

                   


def host_server(ip,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (ip, port)
    print("Iniciando servidor: " +ip+": "+str(port))
    #Reservando porta
    sock.bind(server_address)

    #Escutando na porta reservada
    sock.listen(1)

    #Iniciando protocolo
    while True:
        client, address = sock.accept()
        conexao = threading.Thread(target=listener,args=(client,address,))
        conexao.start()
        # conexao.join()

# while True:
#     print("Digite o número correspondente as opções abaixo")
#     message = input("[1]Host server\n[0]Fechar\n")
#     if message == '0':
#         exit()
#     elif message == '1':
#         ip = input("Digite o ip do servidor: ")
#         port = input("Digite a porta do servidor: ")
#         try:
#             host_server(ip,int(port))
#             break
#         except:
#             print("Não foi possivel criar uma conexão")
#             exit()
host_server('localhost',20002)