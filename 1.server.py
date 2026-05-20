import socket

server = socket.socket()
server.bind(("localhost",7798))
server.listen(1)
print("server waiting...")
conn,addr=server.accept()
print("connected:", addr)
msg = conn.recv(1024).decode()
print("client:", msg)
conn.send("Hello client".encode())
conn.close()
