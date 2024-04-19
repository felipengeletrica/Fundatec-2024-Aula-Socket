import socket

# Definindo o endereço e porta do servidor
HOST = "10.0.1.143"  # Endereço de loopback (localhost)
PORT = 65432  # Porta para escutar

# Criando um socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Vinculando o socket ao endereço e porta especificados
    s.bind((HOST, PORT))
    print("Bind")  # Mensagem de confirmação de vínculo
    # Configurando o socket para escutar conexões entrantes
    s.listen()
    print("Listen")  # Mensagem de confirmação de escuta
    # Aceitando a conexão entrante
    conn, addr = s.accept()
    print("Connected")  # Mensagem de confirmação de conexão
    # Exibindo o endereço do cliente conectado
    print(f"Connected by {addr}")

    # Loop para receber e enviar dados
    while True:
        # Recebendo dados do cliente
        data = conn.recv(1024)
        print(str(data))  # Exibindo os dados recebidos
        if not data:
            break  # Se não houver mais dados, encerra o loop
        # Enviando de volta os dados recebidos para o cliente
        conn.sendall(data)
