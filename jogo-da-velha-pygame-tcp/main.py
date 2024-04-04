import pygame
import socket
import json

from pygame.locals import MOUSEBUTTONDOWN, Rect, QUIT
from sys import exit

def desenhar_tabu():
    pygame.draw.line(tela, (0, 0, 0), (200, 0), (200, 600), 10)
    pygame.draw.line(tela, (0, 0, 0), (400, 0), (400, 600), 10)
    pygame.draw.line(tela, (0, 0, 0), (0, 200), (600, 200), 10)
    pygame.draw.line(tela, (0, 0, 0), (0, 400), (600, 400), 10)

def desenhar_peca(pos):
    global VEZ
    x, y = pos
    if VEZ == 'JOGADOR1':
        pygame.draw.circle(tela, (0, 0, 255), pos, 50,20)
    else:
        img = pygame.image.load('x.png').convert_alpha()
        imgR = pygame.transform.scale(img, (100, 100))
        tela.blit(imgR, (x - 50, y - 50))

def testa_pos():
    for p in rec:
        if e.type == MOUSEBUTTONDOWN and p.collidepoint(mouse_pos):
            if p == rect1:
                confimar(0, [100, 100])
            if p == rect2:
                confimar(1, [300, 100])
            if p == rect3:
                confimar(2, [500, 100])
            if p == rect4:
                confimar(3, [100, 300])
            if p == rect5:
                confimar(4, [300, 300])
            if p == rect6:
                confimar(5, [500, 300])
            if p == rect7:
                confimar(6, [100, 500])
            if p == rect8:
                confimar(7, [300, 500])
            if p == rect9:
                confimar(8, [500, 500])

def confimar(indice, pos):
    global ESCOLHA, VEZ, espaco,ESTADO
    if marca_tabu[indice] == 'X':
        print('X')
    elif marca_tabu[indice] == 'O':
        print('O')
    else:
        marca_tabu[indice] = ESCOLHA
        # desenhar_peca(pos)
        print(marca_tabu)
        if VEZ == 'JOGADOR1':
            VEZ = 'JOGADOR2'
            ESTADO = 'ESPERANDO'
        else:
            VEZ = 'JOGADOR1'
            ESTADO = 'ESPERANDO'
        espaco +=1
        teste = json.dumps({"a":marca_tabu,"b":ESCOLHA, "c":VEZ, "d":espaco,"e":ESTADO,"f":pos})
        connection.send(teste.encode())

def teste_vitoria(l):
    return ((marca_tabu[0] == l and marca_tabu[1] == l and marca_tabu[2] == l) or
        (marca_tabu[3] == l and marca_tabu[4] == l and marca_tabu[5] == l) or
        (marca_tabu[6] == l and marca_tabu[7] == l and marca_tabu[8] == l) or
        (marca_tabu[0] == l and marca_tabu[3] == l and marca_tabu[6] == l) or
        (marca_tabu[1] == l and marca_tabu[4] == l and marca_tabu[7] == l) or
        (marca_tabu[2] == l and marca_tabu[5] == l and marca_tabu[8] == l) or
        (marca_tabu[0] == l and marca_tabu[4] == l and marca_tabu[8] == l) or
        (marca_tabu[2] == l and marca_tabu[4] == l and marca_tabu[6] == l))

def texto_vitoria(v):
    arial = pygame.font.SysFont('arial', 30)
    mensagem = 'JOGADOR {} VENCEU'.format(v)
    if v == 'EMPATE':
        mens_vitoria = arial.render('DEU VELHA', True, (255, 255, 255), (70,70,70))
        tela.blit(mens_vitoria, (0, 300-(arial.get_height()/2)))
    else:
        mens_vitoria = arial.render(mensagem, True, (255, 255, 255), (70,70,70))
        tela.blit(mens_vitoria, (0, 300-(arial.get_height()/2)))

def reset():
        global ESCOLHA, ESTADO, VEZ, marca_tabu, espaco
        ESTADO = 'JOGANDO'
        ESCOLHA = 'X'
        VEZ = 'JOGADOR1'
        espaco = 0
        marca_tabu = [
            0, 1, 2,
            3, 4, 5,
            6, 7, 8
        ]
        tela.fill((255,255,255))

# def pontos(pontos1, pontos2):
#     arial = pygame.font.SysFont('mingliuextbpmingliuextbmingliuhkscsextb', 30)
#     jogador1 = 'Jogador1 = {}'.format(pontos1)
#     jogador2 = 'Jogador2 = {}'.format(pontos2)

#     jd1 = arial.render(jogador1, True, (188, 186, 186))
#     jd2 = arial.render(jogador2, True, (188, 186, 186))
#     tela.blit(jd1, (0, 0))
#     tela.blit(jd2, (420, 0))



ESTADO = 'ESPERANDO'
LOCALPLAYER = False
VEZ = 'JOGADOR1'
ESCOLHA = 'X'
espaco = 0
marca_tabu = [
    0, 1, 2,
    3, 4, 5,
    6, 7, 8
]

pygame.init()
clock = pygame.time.Clock()
tela = pygame.display.set_mode((600, 600), 0, 32)
tela.fill((255,255,255))
pygame.display.set_caption('Jogo da velha')

rect1 = Rect((0, 0), (200, 200))
rect2 = Rect((200, 0), (200, 200))
rect3 = Rect((400, 0), (200, 200))
rect4 = Rect((0, 200), (200, 200))
rect5 = Rect((200, 200), (200, 200))
rect6 = Rect((400, 200), (200, 200))
rect7 = Rect((0, 400), (200, 200))
rect8 = Rect((200, 400), (200, 200))
rect9 = Rect((400, 400), (200, 200))

rec = [
    rect1,rect2,rect3,rect4,
    rect5,rect6,rect7,rect8,rect9,
]

# pontos1, pontos2 = 0, 0

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = ('localhost',20002)
print("Conectando ao servidor")
#Conectando ao servidor
connection.connect(server_address)

while True:
    clock.tick(30)
    mouse_pos = pygame.mouse.get_pos()
    if connection:
        if not LOCALPLAYER:
            connection.send('LOCALPLAYER'.encode())
        data = connection.recv(1024)
        message = data.decode()
        if message == 'LOCALPLAYER1':
            LOCALPLAYER = 'JOGADOR1'
            ESTADO = 'JOGANDO'
        elif message == 'LOCALPLAYER2':
            LOCALPLAYER = 'JOGADOR2'
        elif message != 'waiting':
            filter = message.replace('waiting','')
            if filter != 'LOCALPLAYER1' and filter != 'LOCALPLAYER2' and filter != '':
                teste = json.loads(filter)
                marca_tabu = teste.get("a")
                ESCOLHA = teste.get("b")
                espaco = teste.get("d")
                ESTADO = teste.get("e")
                if LOCALPLAYER == VEZ:
                    ESTADO = 'ESPERANDO'
                else:
                    ESTADO = 'JOGANDO'
                VEZ = teste.get("c")
                desenhar_peca(teste.get("f"))

    if ESTADO == 'JOGANDO':
        desenhar_tabu()
        # pontos(pontos1, pontos2)

        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                exit()
            if e.type == MOUSEBUTTONDOWN:
                if VEZ == 'JOGADOR1' and LOCALPLAYER == VEZ:
                    ESCOLHA = 'X'
                    testa_pos()
                elif VEZ == 'JOGADOR2' and LOCALPLAYER == VEZ:
                    ESCOLHA = 'O'
                    testa_pos()

        if teste_vitoria('X'):
            print('X VENCEU')
            texto_vitoria('X')
            ESTADO = 'RESET'
            # pontos1 += 1

        elif teste_vitoria('O'):
            print('O VENCEU')
            texto_vitoria('O')
            ESTADO = 'RESET'
            # pontos2 +=1

        elif espaco >= 9:
            print('EMPATE')
            texto_vitoria('EMPATE')
            ESTADO = 'RESET'

    elif ESTADO == 'RESET':
        for u in pygame.event.get():
            if u.type == QUIT:
                pygame.quit()
                exit()
            if u.type == MOUSEBUTTONDOWN:
                reset()
                desenhar_tabu()
    elif ESTADO == 'ESPERANDO':
        desenhar_tabu()
        # pontos(pontos1, pontos2)

        for u in pygame.event.get():
            if u.type == QUIT:
                pygame.quit()
                exit()
    else:
        pygame.quit()
        exit()
    connection.send('waiting'.encode())


    pygame.display.flip()