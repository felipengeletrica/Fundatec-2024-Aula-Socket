import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler): # Define uma classe MyTCPHandler que herda de socketserver.BaseRequestHandler. 
                                                     # Esta classe é responsável por lidar com as solicitações dos clientes.
    def handle(self): # Define o método handle(), que será chamado para lidar com cada solicitação de cliente.
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())


if __name__ == "__main__": # Verifica se o script está sendo executado como o programa principal.
    HOST, PORT = "localhost", 65432 # Define o endereço e a porta nos quais o servidor TCP vai escutar.

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.timeout = 10
    server.serve_forever()
