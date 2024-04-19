
import socket
HOST = "10.0.1.193"  # Define o endereço IP (HOST) como o loopback (localhost)
PORT = 65432        # e a porta (PORT) como 65432.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #Cria um novo objeto de socket.
    s.bind((HOST, PORT)) # Associa o socket ao endereço e porta especificados.
    print("Bind") 
    s.listen() # Coloca o socket em modo de escuta, aguardando conexões de entrada.
    print("Listen")
    conn, addr = s.accept() # Aceita uma conexão de entrada e retorna um novo socket (conn) 
                            # para comunicar com o cliente e o endereço do cliente (addr).
    print("Connected")
    with conn: # Cria um contexto para garantir que o socket do cliente seja fechado corretamente após a conclusão da comunicação.
        print(f"Connected by {addr}") # Exibe uma mensagem indicando que uma conexão foi estabelecida, juntamente com o endereço do cliente.
        while True:                     # Loop principal que recebe dados do cliente, os ecoa de volta e continua 
            data = conn.recv(1024)      # até que nenhum dado seja recebido, indicando que a conexão foi fechada pelo cliente.
            print(str(data))
            if not data:
                break
            conn.sendall(data)
