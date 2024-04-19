import socketserver  # Importa o módulo socketserver, que fornece uma infraestrutura para servidores de rede.

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    A classe RequestHandler para o nosso servidor.

    É instanciado uma vez por conexão com o servidor e deve
    substituir o método handle() para implementar a comunicação com o
    cliente.
    """

    def handle(self):
        # self.request é o socket TCP conectado ao cliente
        self.data = self.request.recv(1024).strip()  # Recebe dados do cliente através do socket e remove espaços em branco.
        print("{} wrote:".format(self.client_address[0]))  # Imprime o endereço IP do cliente.
        print(self.data)  # Imprime os dados recebidos do cliente.
        # apenas envia de volta os mesmos dados, mas em maiúsculas
        self.request.sendall(self.data.upper())  # Envia os dados recebidos de volta para o cliente, convertidos para maiúsculas.


if __name__ == "__main__":
    HOST, PORT = "localhost", 65432

    # Cria o servidor, vinculando ao localhost na porta 65432
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)  # Cria um servidor TCP na máquina local (localhost) e na porta 65432, usando a classe MyTCPHandler para lidar com as solicitações.

    # Ativa o servidor; isso continuará em execução até que você
    # interrompa o programa com Ctrl-C
    server.timeout = 10  # Define um timeout de 10 segundos para o servidor.
    server.serve_forever()  # Inicia o servidor e continua executando para sempre, lidando com conexões de clientes.
