# echo-client.py

import socket

HOST = "10.0.1.115"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Seja bem vindo, RAPA!")
    data = s.recv(1024)

print(f"Recebido {str(data)}")
