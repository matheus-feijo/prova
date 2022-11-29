import socket
HOST = '192.168.207.152'     # Endereco IP do Servidor
PORT = 5005            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

print('Para sair use CTRL+X\n')
msg = input()

lista = []

while len(lista) < 100:
    msg = int(input())
    lista.append(msg)

tcp.send(lista)
tcp.close()