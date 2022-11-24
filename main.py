import socket

server = socket.socket()
server.bind(('localhost',9000))
server.listen()

while True:
    con, port=server.accept()
    data=con.recv(1024)
    print('recv:',data)
    con.send(b'HTTP/1.1 200 OK\r\n\r\n')

    with open('../index.html', 'rb') as fr:
        con.send(fr.read())

    con.close()
