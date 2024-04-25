# echo-server.py
import socket
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


# Cria um socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

     # -> Associa o socket a um endereço e porta específicos
    s.bind((HOST, PORT))
    print("Bind")  # -> Mensagem indicando que o bind foi realizado com sucesso


    # -> Coloca o socket em modo de escuta para aceitar conexões entrantes
    s.listen()
    print("Listen") # -> Mensagem indicando que o socket está escutando por conexões

    # -> Aceita a conexão quando um cliente se conecta, criando um novo socket de conexão
    conn, addr = s.accept()
    print("Connected") # Mensagem indicando que uma conexão foi estabelecida
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            print(str(data))
            if not data:
                break
            conn.sendall(data)