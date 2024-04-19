import socketserver  # Importa o módulo socketserver, que fornece uma infraestrutura para servidores de rede.

class MyUDPHandler(socketserver.BaseRequestHandler):
    """
    Esta classe funciona de forma semelhante à classe manipuladora TCP, exceto que
    self.request consiste em um par de dados e soquete do cliente e, como
    não há conexão, o endereço do cliente deve ser fornecido explicitamente
    ao enviar dados de volta via sendto().
    """

    def handle(self):
        data = self.request[0].strip()  # Obtém os dados recebidos do cliente
        socket = self.request[1]  # Obtém o soquete do cliente
        print("{} wrote:".format(self.client_address[0]))  # Imprime o endereço IP do cliente
        print(data)  # Imprime os dados recebidos do cliente
        socket.sendto(data.upper(), self.client_address)  # Envia os dados de volta para o cliente, convertidos para maiúsculas

if __name__ == "__main__":
    HOST, PORT = "localhost", 65431
    
    # Cria um servidor UDP na máquina local (localhost) e na porta 65431, usando a classe MyUDPHandler para lidar com as solicitações.
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        server.serve_forever()  # Inicia o servidor e continua executando para sempre, lidando com conexões de clientes.
