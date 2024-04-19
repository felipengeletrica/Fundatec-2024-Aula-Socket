import socket  # Importa o módulo socket para comunicação de rede.

HOST = "10.0.1.132"  # Endereço IP padrão da interface de loopback (localhost)
PORT = 65432  # Porta para escutar (portas não privilegiadas são > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Cria um objeto socket usando IPv4 (AF_INET) e TCP (SOCK_STREAM)
    
    s.bind((HOST, PORT))  # Associa o socket ao endereço e porta especificados
    print("Bind")
    
    s.listen()  # Coloca o socket em modo de escuta para aceitar conexões
    print("Listen")
    
    conn, addr = s.accept()  # Aceita uma conexão e retorna um novo socket e o endereço do cliente
    print("Connected")
    
    with conn:  # Garante que o socket de conexão seja fechado corretamente quando sair do bloco 'with'
        print(f"Connected by {addr}")  # Imprime o endereço do cliente conectado
        
        while True:
            data = conn.recv(1024)  # Recebe dados do cliente
            print(str(data))  # Imprime os dados recebidos do cliente
            
            if not data:  # Se não houver mais dados a serem recebidos, encerra o loop
                break
            
            conn.sendall(data)  # Envia de volta os dados recebidos para o cliente
