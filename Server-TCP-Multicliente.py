import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    A classe RequestHandler para nosso servidor.
    É instanciada uma vez por conexão com o servidor e deve
    substituir o método handle() para implementar a comunicação
    com o cliente.
    """

    def handle(self):
        # self.request é o socket TCP conectado ao cliente
        self.data = self.request.recv(1024).strip()  # Recebe dados do cliente
        print("{} wrote:".format(self.client_address[0]))  # Exibe o endereço do cliente
        print(self.data)  # Exibe os dados recebidos
        # Envia de volta os mesmos dados em maiúsculas para o cliente
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 65432

    # Cria o servidor, vinculando ao localhost na porta 65432
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Ativa o servidor; ele continuará em execução até que você
    # interrompa o programa com Ctrl-C
    server.timeout = 10  # Define um tempo limite de inatividade de 10 segundos
    server.serve_forever()  # Mantém o servidor em execução indefinidamente
