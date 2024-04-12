# echo-server.py
import socket
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print("Vinculado")
    s.listen()
    print("Escutando")
    conn, addr = s.accept()
    print("Conectando")
    with conn:
        print(f"Conectado por {addr}")
        while True:
            data = conn.recv(1024)
            print(str(data))
            if not data:
                break
            conn.sendall(data)
