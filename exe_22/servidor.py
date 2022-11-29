import socket
HOST = '192.168.207.152'              # Endereco IP do Servidor
PORT = 5005            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)


def ordenaLista(lista):

    return sorted(lista)


while True:
    con, cliente = tcp.accept()
    print('conectado por', cliente)
    while True:
        msg = con.recv(1024)
        if not msg:
            break
        print(cliente, msg)
        values = msg.decode('utf-8')
        print(values)
        resultado = ordenaLista(values)
        con.send(bytes(resultado, 'utf-8'))

    print('Finalizando conexao do cliente', cliente)
    con.close()
