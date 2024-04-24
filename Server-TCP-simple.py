# echo-server.py
import socket
HOST = "192.168.0.21"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print("Bind")
    s.listen()
    print("Listen")
    conn, addr = s.accept()
    print("Connected")
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            print(str(data))
            if not data:
                break
            conn.sendall(data)