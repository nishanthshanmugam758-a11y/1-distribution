import socket
client = socket.socket()
client.connect(("localhost",7798))
client.send("Hello server".encode())
msg = client.recv(1024).decode()
print("server:", msg)
client.close()