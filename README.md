>[!NOTE]
>
>Estes sockets fazem parte das aulas de redes de computadores!

   #  Trabalho socket                                    

## Simple server TCP :

### 1) Subir o tcp server simple explicar os estados da conexão, bind, listen etc.

**Estados de conexão**

* SYN_SENT: o cliente envia uma solicitação de conexão (SYN) para o servidor.
* SYN_RECEIVED: o servidor recebe a solicitação de conexão SYN e responde com sua própria solicitação de conexão SYN, ACK (acknowledgment).
* ESTABLISHED: o cliente recebe a resposta SYN, ACK do servidor e envia um ACK de confirmação. A conexão é estabelecida.

**Escuta e Aceitação de Conexões:**

* LISTENING: o servidor está esperando por conexões de entrada.
* ESTABLISHED: quando uma conexão é aceita pelo servidor, ela entra no estado ESTABLISH.

***
**Métodos utilizados:**

* socket.socket(): Cria um objeto socket. AF_INET indica que estamos usando a família de endereços IPv4 e SOCK_STREAM indica que estamos usando TCP.
* bind(): Liga o socket ao endereço (host) e porta especificados. Isso associa o servidor a uma interface de rede e a uma porta no host.
* listen(): Coloca o socket no modo de escuta, permitindo que aceite conexões de clientes. O argumento especifica o número máximo de conexões pendentes que podem ser enfileiradas para processamento.
* accept(): Aceita uma conexão pendente. Retorna um novo socket (client_socket) e o endereço do cliente (addr), que podem ser usados para enviar e receber dados do cliente.
* send(): Envie dados ao cliente conectado. Aqui, estamos enviando uma mensagem de confirmação ao cliente.
* close(): Fecha o socket.
  

![Listen,Bind](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Tharsila/imagens/Server-TCP-SimplesEstadosCconex%C3%A3o.png?raw=true)

### 2) Executar o programa de cliente simple server tcp e verificar os estados da conexão.

 Executado o "localhost" (192.168.0.21) na porta "65432", envia uma mensagem de teste ("Hello, world!").  
 Apresentando a frase "Hello, world" na tela.  

![Estado conexão](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Tharsila/imagens/clientconexaoserver.png?raw=true)

### 3) Analise o código fonte

```

O primeiro passo é importar o módulo `socket`, que fornece suporte para sockets no Python.  

import socket  

Criação do Socket do Servidor:
Em seguida, criamos um objeto de socket usando socket.socket(). Aqui, especificamos socket.AF_INET para indicar que estamos usando a família de endereços IPv4 e socket.SOCK_STREAM para indicar que estamos usando TCP.    
 **server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)**

Definição do Host e Porta:
A seguir, obtemos o nome da máquina local usando socket.gethostname() e definimos a porta em que o servidor estará escutando conexões.  
 **host = socket.gethostname()port = 12345**  

Vinculação do Socket:  
Usamos o método bind() para vincular o socket ao host e à porta especificados. Isso associa o servidor a uma interface de rede e a uma porta no host.

 **server_socket.bind((host, port))**  

Modo de Escuta:  
Em seguida, usamos o método listen() para colocar o socket no modo de escuta. O argumento passado indica o número máximo de conexões pendentes que podem ser enfileiradas para processamento.  
 **server_socket.listen(5)**

Aceitação de Conexões:  
Entramos em um loop while True para esperar por conexões de clientes. Dentro do loop, usamos o método accept() para aceitar uma conexão pendente. Isso retorna um novo socket (client_socket) que representa a conexão com o cliente e o endereço do cliente (addr).
**while True:
    client_socket, addr = server_socket.accept()**  

Envio de Mensagem ao Cliente:  
Dentro do loop, após aceitar uma conexão, enviamos uma mensagem de confirmação ao cliente usando o método send(). Aqui, a mensagem é codificada em UTF-8 antes de ser enviada.  
**msg = "Conexão estabelecida com o servidor TCP"
client_socket.send(msg.encode('utf-8'))**

Fechamento do Socket do Cliente:  
Após enviar a mensagem, fechamos o socket do cliente usando o método close().  
  **client_socket.close()**

```
---

### 4) Analise usando o wireshark explicando os pacotes.


### 5) Diferencie a conexão UDP de TCP

UDP (User Datagram Protocol) e TCP (Transmission Control Protocol) são dois protocolos de transporte amplamente utilizados na comunicação de redes. Algumas diferenças entre eles:

1. **Confiabilidade e Garantia de Entrega:**
   - TCP: É um protocolo orientado à conexão, garantindo a entrega ordenada e confiável dos dados. Ele faz uso de confirmações e retransmissões para garantir que os dados sejam entregues corretamente e na ordem correta.
   - UDP: É um protocolo não orientado à conexão, o que significa que não há garantia de entrega ou ordem de entrega dos pacotes. Os pacotes podem ser perdidos ou chegar fora de ordem, e não há mecanismo embutido para retransmiti-los automaticamente.

2. **Overhead:**
   - TCP: Devido aos mecanismos de controle de fluxo, controle de congestionamento e garantia de entrega, o TCP tende a ter um overhead maior em comparação com o UDP.
   - UDP: Sendo um protocolo mais simples, o UDP tem um overhead menor em comparação com o TCP.

3. **Conexão:**
   - TCP: Estabelece uma conexão antes de iniciar a transferência de dados. Isso inclui uma fase de handshaking para estabelecer parâmetros de comunicação entre as partes.
   - UDP: Não estabelece uma conexão antes de enviar os dados. Os pacotes podem ser enviados sem a necessidade de handshaking ou estabelecimento de conexão.

4. **Aplicações típicas:**
   - TCP: É mais adequado para aplicações que requerem entrega confiável de dados e controle de fluxo, como transferência de arquivos, navegação na web e email.
   - UDP: É usado em aplicações onde a latência é crítica ou onde a perda de alguns pacotes não é tão crucial, como jogos online, streaming de mídia e voz sobre IP (VoIP).

5. **Velocidade:**
   - TCP: Devido ao seu mecanismo de garantia de entrega e controle de fluxo, o TCP pode ser mais lento em comparação com o UDP, especialmente em redes com alta latência ou perda de pacotes.
   - UDP: Como não há overhead para garantia de entrega e controle de fluxo, o UDP tende a ser mais rápido do que o TCP em situações onde a latência é crítica.

Enquanto o TCP oferece garantia de entrega e controle de fluxo em troca de um overhead maior, o UDP oferece baixa latência e velocidade, mas não garante a entrega dos pacotes. A escolha entre TCP e UDP depende das necessidades específicas da aplicação e das características da rede em questão.


### Simple server UDP :

### 1) Subir o UDP server simple explicar os estados da conexão, bind, listen etc.

 -**bind** O método `socketserver.UDPServer((HOST, PORT), MyUDPHandler)` é utilizado para associar (bind) o servidor a um endereço IP e porta específicos. Isso permite que o servidor escute (listen) por conexões UDP que chegam nesse endereço e porta.

 -**handle** O método `handle(self)` é chamado sempre que o servidor recebe uma mensagem. Ele lida com a mensagem recebida e responde de acordo. Neste caso, ele imprime a mensagem recebida em letras maiúsculas e a envia de volta para o cliente.

 -**client_address** O endereço do cliente é acessado através de `self.client_address`. Isso é útil para saber de onde veio a mensagem recebida.

 -**listen** No UDP, não há um estado de escuta (listen) como no TCP. O servidor está sempre pronto para receber mensagens e não precisa esperar por conexões como no TCP.

No UDP, não há estados de conexão como no TCP. O servidor UDP está sempre pronto para receber mensagens e não mantém uma conexão persistente com os clientes. Ele simplesmente recebe mensagens, processa-as e envia respostas, se necessário. O método bind é usado para associar o servidor a um endereço e porta, mas não há um estado de escuta (listen) no UDP.


### 2) Executar o programa de cliente simple server udp e verificar os estados da conexão.

Para criar um cliente UDP básico, não é necessário verificar estados de conexão. Isso se deve ao fato de que o UDP é um protocolo sem conexão, o que implica que não há necessidade de estabelecer, manter ou encerrar conexões como no TCP. Cada mensagem é tratada de forma independente, e não há garantia de que serão entregues ou recebidas na mesma ordem em que foram enviadas.

Em um cliente UDP, não há "estados de conexão"  para serem verificados.

### 3) Analise o código fonte

```
import socketserver

class MyUDPHandler(socketserver.BaseRequestHandler):
    """
    Esta classe funciona de forma semelhante à classe de manipulador TCP, exceto que
    self.request consiste em um par de dados e soquete do cliente, e como
    não há conexão, o endereço do cliente deve ser fornecido explicitamente
    ao enviar dados de volta via sendto().
    """

    def handle(self):
        # Recebe os dados e o soquete do cliente
        data = self.request[0].strip()
        socket = self.request[1]
        
        # Imprime os dados recebidos
        print("{} escreveu:".format(self.client_address[0]))
        print(data)
        
        # Envia de volta os dados em maiúsculas para o cliente
        socket.sendto(data.upper(), self.client_address)

if __name__ == "__main__":
    # Define o endereço do servidor e a porta
    HOST, PORT = "localhost", 65431
    
    # Cria um servidor UDP com o endereço e a porta especificados, usando MyUDPHandler para lidar com as solicitações
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        # Mantém o servidor em execução continuamente
        server.serve_forever()

```

- **socketserver.BaseRequestHandler**: Esta é uma classe base fornecida pelo módulo `socketserver` do Python para lidar com solicitações de clientes. Aqui, estamos criando uma subclasse chamada `MyUDPHandler`.

- **handle(self)**: Este método é chamado quando uma solicitação é recebida. Aqui, estamos recebendo os dados e o soquete do cliente, imprimindo os dados recebidos e enviando de volta os dados em maiúsculas para o cliente.

- **if __name__ == "__main__"**: Esta é uma construção comum em Python para verificar se o script está sendo executado como um programa principal. Se for o caso, o código dentro deste bloco será executado.

- **socketserver.UDPServer((HOST, PORT), MyUDPHandler)**: Aqui, estamos criando um servidor UDP na máquina local (`localhost`) e na porta especificada (`65431`). Estamos passando a classe `MyUDPHandler` como o manipulador de solicitações para o servidor.

- **server.serve_forever()**: Este método mantém o servidor em execução continuamente, lidando com solicitações de clientes conforme elas chegam.


### 4) Analise usando o wireshark explicando os pacotes.

***

## Multiserver TCP :

### 1) Subir o tcp server simple explicar os estados da conexão, bind, listen etc.

- **Bind (bind()):**
  - Usamos o método `bind()` para vincular o socket ao endereço (HOST) e à porta (PORT) especificados. Isso associa o servidor a uma interface de rede e a uma porta no host.

- **Modo de Escuta (listen()):**
  - Utilizamos o método `listen()` para colocar o socket no modo de escuta. O argumento passado indica o número máximo de conexões pendentes que podem ser enfileiradas para processamento.

- **Aceitação de Conexões (accept()):**
  - Entramos em um loop infinito onde aguardamos e aceitamos conexões de clientes usando o método `accept()`. Quando uma conexão é aceita, um novo socket (`client_socket`) é criado para se comunicar com o cliente e o endereço do cliente (`client_address`) é retornado.

- **Lida com Clientes (handle_client()):**
  - Cada conexão de cliente é tratada em uma nova thread utilizando a função `handle_client()`. Dentro dessa função, podemos realizar operações de leitura e escrita de dados com o cliente.

Esses são os principais aspectos a serem considerados ao subir um servidor TCP multi-cliente.Lidar com múltiplos clientes simultaneamente.


### 2) Executar o programa de cliente simple server tcp e verificar os estados da conexão.

Executado via "localhost" ( 192.168.0.21) na porta "65432", envia uma mensagem de teste ("Hello, world!").

As quatro primeiras primitivas na lista são executadas pelos servidores a primitiva SOCKET cria um novo ponto final e aloca espaço de tabela para ele na entidade de transporte.

O valor que é recebido "Hello, world".

![Cliete Tcp](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Tharsila/imagens/02ClientUDP.jpg?raw=true)

### 3) Analise o código fonte

```
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()  # Recebe dados do cliente
        print("{} wrote:".format(self.client_address[0]))  # Imprime o endereço do cliente
        print(self.data)  # Imprime os dados recebidos do cliente
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())  # Envia os dados recebidos de volta ao cliente em maiúsculas


if __name__ == "__main__":
    HOST, PORT = "localhost", 65432

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.timeout = 10  # Define um tempo limite para as conexões
    server.serve_forever()  # Mantém o servidor em execução continuamente

```

- **Classe MyTCPHandler:**
  - Esta classe é uma subclasse de `socketserver.BaseRequestHandler`, que é usada para manipular solicitações de clientes. O método `handle()` precisa ser sobrescrito para implementar a comunicação com o cliente.

- **Método handle():**
  - Dentro deste método, os dados recebidos do cliente são processados. Primeiro, os dados são recebidos usando `self.request.recv(1024)`, e em seguida são impressos na tela. Depois, os dados são enviados de volta para o cliente, mas em maiúsculas, usando `self.request.sendall(self.data.upper())`.

- **Configuração do Servidor:**
  - O servidor é criado usando `socketserver.TCPServer`, onde especificamos o HOST e a PORTA para a ligação. Em seguida, chamamos `server.serve_forever()` para ativar o servidor e fazê-lo escutar continuamente por novas conexões de clientes.


### 4) Analise usando o wireshark explicando os pacotes.

### 5) Explique as diferenças de multi conexões e porque a cada conexão a porta "muda". Demonstre a mudança de porta usando o Wireshark

Em redes de computadores, multi-conexões permitem que dispositivos estabeleçam várias comunicações simultâneas. Cada conexão é identificada por uma porta única, que muda a cada nova conexão para evitar conflitos e garantir a segurança das comunicações.

![Mult](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Tharsila/imagens/03ClientUDP.jpg?raw=true)

***
## Conexão com máquina remota do colega :

### 1) Subir o tcp server na máquina do colega, verificar o IP da máquina (certifique que ele esteja na mesma rede que você)

O servidor TCP foi configurado e em execução na máquina do meu colega. Inseri o endereço IP  e a porta específica na qual o servidor está ouvindo. E obtivi a permissão do meu colega antes de realizar a conexão.

### 2) Executar o programa cliente na sua máquina, não esqueça de modificar o IP para a máquina do seu colega.

Para executar o programa cliente na minha máquina, me  certifiquei de modificar o endereço IP para o da máquina do seu colega. Depois disso, bastou iniciar o cliente e ele  se conectar automaticamente ao servidor na máquina do colega.

### 3) Demonstre com imagens que a conexão teve sucesso.
***Server

![Server](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Tharsila/imagens/01ServerTCP.jpg?raw=true)

***Client

![Client](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Tharsila/imagens/02ClientUDP.jpg?raw=true)

### 4) Usando wireshark mostra conexão filtrando pela portas.

Aqui conseguimos ver a mensagem envia, filtrando pelas portas no wireshark.

![conex](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Tharsila/imagens/02ServerTCP.jpg?raw=true)




