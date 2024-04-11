import socket

HOST, PORT = "localhost", 65431

# SOCK_DGRAM is the socket type to use for UDP sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = input("Mensagem:")
    # As you can see, there is no connect() call; UDP has no connections.
    # Instead, data is directly sent to the recipient via sendto().
    sock.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
    received = str(sock.recv(1024), "utf-8")

    print("Enviar:     {}".format(data))
    print("Recebido: {}".format(received))
