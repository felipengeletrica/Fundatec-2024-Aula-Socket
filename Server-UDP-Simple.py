import socketserver

class MyUDPHandler(socketserver.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle(self):
       # -> Define um método handle para lidar com as solicitações de clientes
        data = self.request[0].strip() 

        socket = self.request[1]  # -> Obtém o socket do cliente
        print("{} wrote:".format(self.client_address[0]))  
        
        print(data)  # -> Imprime os dados recebidos do cliente
        socket.sendto(data.upper(), self.client_address)  

if __name__ == "__main__":
    # -> Executa o código abaixo apenas se este script for executado diretamente, não se for importado como um módulo

    HOST, PORT = "localhost", 65431  # -> Define o host (localhost) e a porta (65431) em que o servidor UDP será executado

    # -> Cria um servidor UDP na interface definida pelo host e porta especificada, usando a classe MyUDPHandler para lidar com as solicitações
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        server.serve_forever()