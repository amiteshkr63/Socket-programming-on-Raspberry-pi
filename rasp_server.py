import socket
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.bind(("127.0.0.1",1234))
mysock.listen(5)
conn, addr=mysock.accept()
while True:
    data=conn.recv(1000)
    if not data:
        continue
    conn.sendall(data)