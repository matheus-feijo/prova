import socket
HOST = '192.168.207.152'              # Endereco IP do Servidor
PORT = 5005            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

def sequenciaNumeros(value):
    lista = []
    for i in range(0,value['tamanho']):
        lista.append(i + value['indice'])

    return lista

while True:
    con, cliente = tcp.accept()
    print ('conectado por', cliente)
    while True:
        msg = con.recv(1024)
        if not msg: break
        print(cliente, msg)
        value = msg.decode('utf-8')
        print(value)
        resultado = sequenciaNumeros(value)
        con.send(bytes(resultado, 'utf-8'))

    print('Finalizando conexao do cliente', cliente)
    con.close()


#value = {
 #   'tamanho':10,
 #   'indice':5,
#}





