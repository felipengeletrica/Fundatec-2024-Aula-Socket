import socketserver

class MyUDPHandler(socketserver.BaseRequestHandler): #Define uma classe MyUDPHandler que herda de socketserver.BaseRequestHandler. 
                                                     #Esta classe é responsável por lidar com as solicitações dos clientes.
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """
    def handle(self): # Define o método handle(), que será chamado para lidar com cada solicitação de cliente.
        data = self.request[0].strip() # Recebe os dados enviados pelo cliente. No caso de UDP, self.request é uma tupla 
                                       # contendo os dados recebidos e o socket do cliente. Aqui, data contém os dados 
                                       # recebidos, que são posteriormente limpos (stripped) de espaços em branco.
        socket = self.request[1] # Obtém o socket do cliente a partir da tupla self.request.
        print("{} wrote:".format(self.client_address[0])) # Exibe o endereço IP do cliente que enviou os dados e os próprios
                                                          # dados no console do servidor.
        print(data)
        socket.sendto(data.upper(), self.client_address) # Converte os dados recebidos para maiúsculas e os envia de volta para o 
                                                         # cliente usando o método sendto(). É necessário fornecer explicitamente 
                                                         # o endereço do cliente para enviar os dados, pois o UDP não mantém uma 
                                                         # conexão persistente.

if __name__ == "__main__": # Verifica se o script está sendo executado como o programa principal.
    HOST, PORT = "localhost", 65431 # Define o endereço e a porta nos quais o servidor UDP vai escutar.
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server: # Cria uma instância do servidor UDP, 
                                                                       # passando o endereço e a classe de manipulador MyUDPHandler.
        server.serve_forever() # Inicia o servidor e o mantém em execução indefinidamente.
