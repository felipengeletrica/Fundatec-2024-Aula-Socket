import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
         # -> Define um método handle para lidar com as solicitações de clientes
        self.data = self.request.recv(1024).strip()  # -> Recebe dados do cliente
        
        print("{} wrote:".format(self.client_address[0]))  # -> Imprime o endereço IP do cliente
        print(self.data)  # -> Imprime os dados recebidos do cliente
        self.request.sendall(self.data.upper())  # -> Envia os dados recebidos de volta ao cliente em letras maiúsculas


if __name__ == "__main__":
    # -> Executa o código abaixo apenas se este script for executado diretamente, não se for importado como um módulo

    HOST, PORT = "localhost", 65432  # Define o host (localhost) e a porta (65432) em que o servidor TCP será executado

    # -> Cria um servidor TCP na interface definida pelo host e porta especificada, usando a classe MyTCPHandler para lidar com as solicitações
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    server.timeout = 10  # -> Define um tempo limite de 10 segundos para as conexões
    server.serve_forever()  # -> Inicia o servidor e o mantém em execução indefinidamente