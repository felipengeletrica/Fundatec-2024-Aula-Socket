import socketserver

class MyUDPHandler(socketserver.BaseRequestHandler):
    """
    Esta classe funciona de forma semelhante à classe de manipulador TCP, exceto que
    self.request consiste em um par de dados e um socket do cliente, e como
    não há conexão, o endereço do cliente deve ser fornecido explicitamente
    ao enviar dados de volta via sendto().
    """

    def handle(self):
        # Extrai os dados recebidos e o socket do cliente
        data = self.request[0].strip()  # Extrai os dados
        socket = self.request[1]  # Extrai o socket do cliente
        # Exibe o endereço do cliente e os dados recebidos
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        # Envia de volta os dados em maiúsculas para o cliente
        socket.sendto(data.upper(), self.client_address)

if __name__ == "__main__":
    HOST, PORT = "localhost", 65431

    # Cria o servidor UDP, vinculando ao localhost na porta 65431
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        # Ativa o servidor; ele continuará em execução até que você
        # interrompa o programa com Ctrl-C
        server.serve_forever()
