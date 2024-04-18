Estes sockets fazem parte das aulas de redes de computadores!

Enjoy meus alunos!

Alunos!!!

# Trabalho socket

Estes sockets fazem parte das aulas de redes de computadores!
Enjoy meus alunos!

Alunos!!!
***
## Sobre o trabalho

Documente com print e coloque aqui as respostas

### Simple server TCP :

1) Subir o tcp server simple explicar os estados da conexão, bind, listen etc.

Este código Python é um servidor TCP simples que ecoa de volta qualquer mensagem que recebe do cliente.
Importando o Módulo Socket:
python
Copy code
import socket
Aqui, estamos importando o módulo socket, que fornece as funcionalidades necessárias para criar e gerenciar sockets em Python.
Definindo o Endereço e Porta do Servidor:
python
Copy code
HOST = "10.0.1.131"  # Endereço do host
PORT = 65432  # Porta para escutar
Estamos definindo o endereço IP do host como 10.0.1.131 e a porta como 65432. O servidor irá escutar por conexões nesta porta.
Criando um Socket:
python
Copy code
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
Estamos criando um socket TCP IPv4 usando socket.AF_INET e socket.SOCK_STREAM. O uso do gerenciador de contexto with garante que o socket seja fechado corretamente após o uso.
Fazendo o Bind:
python
Copy code
s.bind((HOST, PORT))
Aqui, estamos associando o socket ao endereço e porta especificados. O servidor estará disponível neste endereço e porta para receber conexões de entrada.
Colocando em Modo de Escuta (Listen):
python
Copy code
s.listen()
Esta função coloca o socket em modo de escuta, permitindo que aceite conexões de entrada. O servidor está agora esperando por conexões de clientes.
Aceitando Conexões de Entrada:
python
Copy code
conn, addr = s.accept()
Quando uma conexão de entrada é recebida, a função accept() é chamada, que aceita a conexão e retorna um novo socket conn dedicado à comunicação com o cliente, e o endereço addr do cliente.
Comunicando com o Cliente:
python
Copy code
with conn:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
Neste trecho, estamos recebendo dados do cliente através do socket conn, ecoando de volta esses dados para o cliente e repetindo esse processo enquanto houver dados a serem recebidos.
Fechando a Conexão:
O uso do gerenciador de contexto with garante que o socket conn seja fechado automaticamente após a comunicação ser concluída.
Este servidor TCP simples passa pelos seguintes estados:

Bind: Associa o socket a um endereço e porta.
Listen: Coloca o socket em modo de escuta, esperando por conexões de entrada.
Accept: Aceita uma conexão de entrada e cria um novo socket dedicado para comunicação com o cliente.
Connected: Indica que uma conexão foi estabelecida com sucesso entre o servidor e o cliente.

2) Executar o programa de cliente simple server tcp e verificar os estados da conexão.
Bind
Listen

3) Analise o código fonte
Importando o Módulo socketserver:
python
Copy code
import socketserver
Aqui, estamos importando o módulo socketserver, que nos permite criar facilmente servidores de socket em Python.
Definindo a Classe MyUDPHandler:
python
Copy code
class MyUDPHandler(socketserver.BaseRequestHandler):
Esta classe é uma subclasse de socketserver.BaseRequestHandler e serve para manipular as solicitações recebidas pelo servidor UDP.
Docstring da Classe:
python
Copy code
"""
This class works similar to the TCP handler class, except that
self.request consists of a pair of data and client socket, and since
there is no connection the client address must be given explicitly
when sending data back via sendto().
"""
Aqui, temos uma docstring que descreve a funcionalidade da classe. Ela explica que a classe é semelhante à classe de manipulador TCP, mas trabalha com UDP. Também destaca que, como não há conexão estabelecida, o endereço do cliente deve ser explicitamente fornecido ao enviar dados de volta.
Método handle():
python
Copy code
def handle(self):
    data = self.request[0].strip()
    socket = self.request[1]
    print("{} wrote:".format(self.client_address[0]))
    print(data)
    socket.sendto(data.upper(), self.client_address)
O método handle() é chamado quando uma nova solicitação é recebida pelo servidor UDP. Ele processa a solicitação e envia uma resposta ao cliente. Aqui está o que está acontecendo dentro do método:
data = self.request[0].strip(): Extrai os dados recebidos do cliente, removendo quaisquer espaços em branco no início e no final.
socket = self.request[1]: Extrai o socket associado à solicitação do cliente.
print("{} wrote:".format(self.client_address[0])): Imprime o endereço IP do cliente que enviou os dados.
print(data): Imprime os dados recebidos do cliente.
socket.sendto(data.upper(), self.client_address): Converte os dados recebidos para maiúsculas e os envia de volta para o cliente usando socket.sendto(), fornecendo o endereço do cliente explicitamente.
Bloco de Execução Principal:
python
Copy code
if __name__ == "__main__":
    HOST, PORT = "localhost", 65431
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        server.serve_forever()
Neste bloco, estamos inicializando o servidor UDP. O servidor é configurado para escutar em localhost (127.0.0.1) na porta 65431. Em seguida, entramos em um loop infinito para que o servidor esteja sempre pronto para receber e processar solicitações de clientes.
Resumindo, este código implementa um servidor UDP simples em Python que recebe mensagens de clientes, converte as mensagens para maiúsculas e as envia de volta para os clientes. Ele usa a classe socketserver.BaseRequestHandler para definir o comportamento do servidor ao lidar com solicitações de clientes UDP.

4) Analise usando o wireshark explicando os pacotes.

5) Diferencie a conexão UDP de TCP
TCP (Transmission Control Protocol):
Confiabilidade: TCP é um protocolo orientado à conexão, o que significa que é altamente confiável. Ele garante que os dados sejam entregues na ordem correta e sem erros.
Controle de Fluxo: TCP implementa controle de fluxo, o que evita que o remetente sobrecarregue o receptor com dados muito rapidamente. Ele ajusta a taxa de transmissão com base na capacidade do receptor de processar os dados.
Controle de Congestionamento: Além do controle de fluxo, TCP também lida com o controle de congestionamento. Ele ajusta a taxa de transmissão com base na condição da rede, evitando congestionamentos e garantindo uma melhor utilização da largura de banda disponível.
Handshake de Conexão: Antes de iniciar a transferência de dados, TCP estabelece uma conexão bidirecional entre o cliente e o servidor por meio de um handshake de três vias (SYN, SYN-ACK, ACK). Isso garante que ambos os lados estejam prontos para enviar e receber dados.
Orientado a Bytes: TCP é orientado a bytes, o que significa que os dados são transmitidos em sequência, e o receptor recebe os bytes na mesma ordem em que foram enviados.
Overhead: TCP tem um overhead maior em comparação com UDP devido aos mecanismos de garantia de entrega, controle de fluxo e controle de congestionamento.
UDP (User Datagram Protocol):
Não Orientado à Conexão: UDP é um protocolo não orientado à conexão, o que significa que ele não estabelece uma conexão antes de enviar os dados. Os pacotes são simplesmente enviados para o destino sem garantia de entrega ou ordem.
Sem Garantia de Entrega: UDP não oferece garantia de entrega dos dados. Os pacotes podem ser perdidos, duplicados ou entregues fora de ordem. Não há mecanismos embutidos para detecção ou correção de erros.
Sem Controle de Fluxo ou Congestionamento: Ao contrário do TCP, UDP não implementa controle de fluxo ou controle de congestionamento. Isso significa que os dados são enviados na taxa máxima possível, independentemente da capacidade da rede.
Baixo Overhead: UDP tem um overhead menor em comparação com TCP devido à falta de mecanismos de controle e garantia de entrega.
Ideal para Aplicações de Tempo Real: Devido à sua baixa latência e falta de overhead, UDP é frequentemente usado em aplicações de tempo real, como jogos online, transmissão de vídeo e voz sobre IP (VoIP), onde a latência é crítica e uma pequena perda de dados é aceitável.
***

### Simple server UDP :

1) Subir o tcp server simple explicar os estados da conexão, bind, listen etc.
Este código é um servidor UDP simples em Python usando o módulo socketserver. Vamos entender cada parte e o que o código faz:

Importando o Módulo socketserver:
python
Copy code
import socketserver
O módulo socketserver fornece classes para criar servidores de socket de maneira mais fácil e intuitiva.
Definindo a Classe MyUDPHandler:
python
Copy code
class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
Esta classe é uma subclasse de socketserver.BaseRequestHandler, que define como lidar com solicitações de cliente. Aqui, estamos substituindo o método handle(), que é chamado sempre que uma nova solicitação é recebida pelo servidor.
Tratamento da Solicitação UDP:
python
Copy code
    data = self.request[0].strip()
    socket = self.request[1]
Dentro do método handle(), estamos recebendo os dados enviados pelo cliente e o socket associado à solicitação. Os dados recebidos são armazenados na variável data, e o socket é armazenado na variável socket.
Processamento dos Dados e Resposta:
python
Copy code
    print("{} wrote:".format(self.client_address[0]))
    print(data)
    socket.sendto(data.upper(), self.client_address)
Aqui, estamos imprimindo os dados recebidos e o endereço IP do cliente que os enviou. Em seguida, estamos convertendo os dados para maiúsculas usando data.upper() e enviando de volta para o cliente usando socket.sendto(). O endereço do cliente é necessário para enviar a resposta de volta para o cliente correto.
Configuração do Servidor UDP:
python
Copy code
if __name__ == "__main__":
    HOST, PORT = "localhost", 65431
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        server.serve_forever()
Aqui, estamos configurando o servidor UDP para escutar em um endereço e porta específicos. O servidor é iniciado com socketserver.UDPServer((HOST, PORT), MyUDPHandler), onde HOST é o endereço IP do servidor e PORT é a porta. Em seguida, o servidor é colocado em um loop infinito usando server.serve_forever(), o que significa que ele continuará a receber e processar solicitações de clientes indefinidamente.


2) Executar o programa de cliente simple server tcp e verificar os estados da conexão.

Entendendo o Cliente TCP:
O cliente TCP é um programa que se conecta a um servidor TCP em uma determinada máquina e porta. Ele pode enviar dados para o servidor e receber respostas. No nosso caso, o cliente TCP que estamos usando é um programa simples em Python.
Executando o Cliente TCP:
Para executar o cliente TCP, você precisa seguir estas etapas:
Abra um ambiente de desenvolvimento Python, como o IDLE ou um terminal.
Cole o código do cliente TCP no ambiente de desenvolvimento.
Certifique-se de modificar o código do cliente para usar o endereço IP e a porta corretos do servidor TCP que deseja se conectar. Por exemplo, se o servidor estiver em localhost (o mesmo computador em que você está executando o cliente) e estiver escutando na porta 8080, você deve definir HOST = 'localhost' e PORT = 8080.
Execute o código do cliente.
Verificando os Estados da Conexão:
Durante a execução do cliente TCP, você pode verificar os estados da conexão observando as mensagens impressas no console. Aqui estão os estados comuns que você pode encontrar e o que significam:
Conexão Estabelecida: Isso significa que o cliente conseguiu se conectar com sucesso ao servidor. Isso indica que o servidor está ativo e aceitando conexões na porta especificada.
Conexão Encerrada: Isso indica que o cliente encerrou a conexão com o servidor. Pode acontecer imediatamente após a conexão ser estabelecida, dependendo do que o cliente está programado para fazer. Isso não indica necessariamente um problema, a menos que seja inesperado.
Interpretando os Resultados:
Se você vir "Conexão Estabelecida", isso é um bom sinal de que o cliente conseguiu se conectar ao servidor com sucesso.
Se você vir "Conexão Encerrada", pode significar que o cliente completou sua tarefa e encerrou a conexão de forma adequada. No entanto, se isso acontecer imediatamente após "Conexão Estabelecida" e não for esperado, pode ser necessário investigar se há algum problema na comunicação.
Depuração e Solução de Problemas:
Se o cliente não conseguir se conectar ao servidor ou se a conexão for encerrada inesperadamente, você pode precisar fazer algumas verificações:
Verifique se o servidor está ativo e escutando na porta especificada.
Verifique se o endereço IP e a porta no cliente estão corretos e correspondem aos do servidor.
Verifique se não há firewall ou restrições de rede que estejam bloqueando a comunicação entre o cliente e o servidor.

3) Analise o código fonte
Importando o Módulo socketserver:
python
Copy code
import socketserver
O módulo socketserver fornece classes para criar facilmente servidores de socket em Python.
Definindo a Classe MyUDPHandler:
python
Copy code
class MyUDPHandler(socketserver.BaseRequestHandler):
Esta classe é uma subclasse de socketserver.BaseRequestHandler e define o comportamento do servidor para manipular solicitações de clientes UDP.
Docstring da Classe:
python
Copy code
"""
This class works similar to the TCP handler class, except that
self.request consists of a pair of data and client socket, and since
there is no connection the client address must be given explicitly
when sending data back via sendto().
"""
Este é o docstring da classe, uma string de documentação que explica o propósito da classe e seu funcionamento. Ele descreve que a classe é semelhante à classe de manipulador TCP, mas lida com conexões UDP, onde não há conexão estabelecida entre o servidor e o cliente.
Método handle():
python
Copy code
def handle(self):
    data = self.request[0].strip()
    socket = self.request[1]
    print("{} wrote:".format(self.client_address[0]))
    print(data)
    socket.sendto(data.upper(), self.client_address)
O método handle() é chamado sempre que o servidor recebe uma solicitação de um cliente UDP. Ele é responsável por processar a solicitação e enviar uma resposta ao cliente.
data = self.request[0].strip(): Extrai os dados recebidos do cliente, removendo quaisquer espaços em branco do início e do final.
socket = self.request[1]: Extrai o socket associado à solicitação do cliente.
print("{} wrote:".format(self.client_address[0])): Imprime o endereço IP do cliente que enviou os dados.
print(data): Imprime os dados recebidos do cliente.
socket.sendto(data.upper(), self.client_address): Converte os dados recebidos para maiúsculas e envia-os de volta para o cliente usando socket.sendto(), fornecendo o endereço do cliente explicitamente.
Bloco de Execução Principal:
python
Copy code
if __name__ == "__main__":
    HOST, PORT = "localhost", 65431
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        server.serve_forever()
Este bloco é o ponto de entrada do programa. Ele define o endereço e a porta em que o servidor UDP irá escutar por solicitações de clientes e inicializa o servidor UDP usando a classe socketserver.UDPServer. Em seguida, o servidor é colocado em um loop infinito usando server.serve_forever(), o que significa que ele continuará a receber e processar solicitações de clientes indefinidamente.
Em resumo, este código implementa um servidor UDP simples em Python que recebe mensagens de clientes, converte as mensagens para maiúsculas e as envia de volta para os clientes. Ele usa a classe socketserver.BaseRequestHandler para definir o comportamento do servidor ao lidar com solicitações de clientes UDP.

4) Analise usando o wireshark explicando os pacotes.

***

### Multiserver TCP :

1) Subir o tcp server simple explicar os estados da conexão, bind, listen etc.
Criação do Socket:
python
Copy code
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
socket.AF_INET indica que estamos utilizando IPv4.
socket.SOCK_STREAM indica que estamos criando um socket TCP.
Bind:
python
Copy code
server_socket.bind((HOST, PORT))
A função bind() associa o socket a um endereço (HOST) e porta (PORT). Isso indica ao sistema operacional onde o servidor vai escutar por conexões de entrada.
Listen:
python
Copy code
server_socket.listen()
A função listen() coloca o socket em modo de escuta, permitindo que ele aceite conexões de entrada.
Accept:
python
Copy code
client_socket, client_address = server_socket.accept()
A função accept() bloqueia o programa e aguarda a chegada de uma conexão de cliente. Quando uma conexão é recebida, ela é aceita e um novo socket (client_socket) é criado para se comunicar com o cliente. client_address armazena o endereço do cliente.
Fechando o Socket do Servidor:
python
Copy code
print("Fechando o socket do servidor")
Após a comunicação com o cliente, o socket do servidor pode ser fechado. Este passo é opcional e depende da lógica do seu aplicativo.

2) Executar o programa de cliente simple server tcp e verificar os estados da conexão.

Neste script, que é executado localmente através do endereço "localhost" (127.0.0.1) e na porta "65432", é enviado uma mensagem de teste, que neste caso é "Hello, world!".

As quatro primeiras operações na lista são realizadas pelos servidores nessa sequência: a operação de criação de SOCKET estabelece um novo ponto de extremidade e reserva espaço de tabela para ele na entidade de transporte.

As configurações de chamada determinam o formato de endereçamento a ser utilizado, o tipo de serviço desejado (como um fluxo de bytes confiável) e o protocolo a ser utilizado.

Uma chamada de SOCKET bem-sucedida retorna um identificador de arquivo comum, que será empregado em chamadas posteriores, semelhante a uma chamada OPEN em seu funcionamento.

Em seguida, a mensagem recebida "Hello, world" é apresentada na tela.

3) Analise o código fonte
Importação do Módulo socketserver:
python
Copy code
import socketserver
Aqui, estamos importando o módulo socketserver, que fornece classes para criar servidores de socket de maneira mais fácil em Python.
Definição da Classe MyTCPHandler:
python
Copy code
class MyTCPHandler(socketserver.BaseRequestHandler):
Esta classe é uma subclasse de socketserver.BaseRequestHandler e define o comportamento do servidor para manipular solicitações de clientes TCP.
Docstring da Classe:
python
Copy code
"""
The RequestHandler class for our server.

It is instantiated once per connection to the server, and must
override the handle() method to implement communication to the
client.
"""
Aqui, temos uma docstring que descreve o propósito da classe. Ela explica que a classe é responsável por lidar com solicitações de clientes no servidor e que a função handle() deve ser implementada para realizar a comunicação com o cliente.
Método handle():
python
Copy code
def handle(self):
    self.data = self.request.recv(1024).strip()
    print("{} wrote:".format(self.client_address[0]))
    print(self.data)
    self.request.sendall(self.data.upper())
O método handle() é chamado sempre que o servidor recebe uma solicitação de um cliente TCP. Ele processa a solicitação e envia uma resposta de volta ao cliente. Aqui está o que está acontecendo dentro do método:
self.request.recv(1024): Recebe dados do cliente, com um limite de 1024 bytes.
print("{} wrote:".format(self.client_address[0])): Imprime o endereço IP do cliente que enviou os dados.
print(self.data): Imprime os dados recebidos do cliente.
self.request.sendall(self.data.upper()): Envia de volta ao cliente os dados recebidos convertidos para letras maiúsculas.
Bloco de Execução Principal:
python
Copy code
if __name__ == "__main__":
    HOST, PORT = "localhost", 65432
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.timeout = 10
    server.serve_forever()
Neste bloco, estamos inicializando o servidor TCP. O servidor é configurado para escutar em localhost (127.0.0.1) na porta 65432. Em seguida, entramos em um loop infinito usando server.serve_forever(), o que significa que ele continuará a receber e processar solicitações de clientes indefinidamente.
Este código cria um servidor TCP que recebe mensagens de clientes, converte as mensagens para maiúsculas e as envia de volta para os clientes. Ele ilustra o uso do módulo socketserver para simplificar a criação de servidores de socket em Python.


4) Analise usando o wireshark explicando os pacotes.

5) Explique as diferenças de multi conexões e porque a cada conexão a porta "muda". Demonstre a mudança de porta usando o Wireshark

***
### Conexão com máquina remota do colega :

1) Subir o tcp server na máquina do colega, verificar o IP da máquina (certifique que ele esteja na mesma rede que você)
[![Print Screm](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Tharsila/imagens/01ServerTCP.jpg)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Tharsila/imagens/01ServerTCP.jpg)

2) Executar o programa cliente na sua máquina, não esqueça de modificar o IP para a máquina do seu colega.

3) Demonstre com imagens que a conexão teve sucesso.

4) Usando wireshark mostra conexão filtrando pela portas.

***
Exemplo colocando código

```python
# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {str(data)}")
```



