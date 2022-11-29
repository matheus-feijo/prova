import socket
HOST = '192.168.207.152'     # Endereco IP do Servidor
PORT = 5005            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

print('Para sair use CTRL+X\n')
msg = input()

lista = []

n = int(input('Digite um valor para n: '))


for i in range(0, n, 1):
    value = int(input('value: '))
    lista.append(value)


p = int(input('Digite um valor para p: '))

data = {lista, p}


tcp.send(data)
tcp.close()
