# TRABALHO SOCKET 

Trabalho Sockets que faz parte da aula de Redes.

#### Aluno: Artur Bazzanella Christmann
#### Professor: Felipe Vargas
#### Turma: TI23

***

### Sobre o trabalho

Documente com print e coloque aqui as respostas

### Simple server TCP :

### 1) Subir o tcp server simple explicar os estados da conexão, bind, listen etc.

#### Resposta 1:

Ao subir o Servidor Simples com o comando "python Server-TCP-simple.py", que é executado através de um script em Python, o serviço primitivo de transporte de soquetes TCP é iniciado. Isso envolve os seguintes estados da conexão:

Bind: O servidor associa um endereço local (por exemplo, um endereço IP ou DNS, neste caso "localhost", e um número de porta, que neste script é a porta 65432) ao soquete.

Listen: O servidor fica pronto para receber conexões entrantes, anunciando a disponibilidade para conexão e especificando o tamanho da fila de conexões pendentes.

Com isso, o servidor está pronto para estabelecer conexões ativas, enviar e receber dados através delas.

#### Print Screem:
[![Print Screm](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/01-Start-PY-Server.jpg)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/01-Start-PY-Server.jpg)

### 2) Executar o programa de cliente simple server tcp e verificar os estados da conexão.

#### Resposta 2:

Neste script, que é executado via "localhost" (127.0.0.1) na porta "65432", envia uma mensagem de teste ("Hello, world!").

As quatro primeiras primitivas na lista são executadas pelos servidores nessa ordem: a primitiva SOCKET cria um novo ponto final e aloca espaço de tabela para ele na entidade de transporte.

Os parâmetros da chamada especificam o formato de endereçamento a ser usado, o tipo de serviço desejado (por exemplo, um fluxo de bytes confiável) e o protocolo.

Uma chamada SOCKET bem-sucedida retorna um descritor de arquivo comum que será usado nas chamadas subsequentes, exatamente como uma chamada OPEN.

Apresentando na tela o valor recebido "Hello, world".

#### Print Screem:
[![Print Screm](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/02-Hello-World.jpg)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/02-Hello-World.jpg)

### 3) Analise o código fonte

#### Resposta 3:

Os códigos consistem em um servidor TCP simples (echo-server.py) e um cliente TCP (echo-client.py) que se comunicam entre si. O servidor aguarda por conexões e, quando uma conexão é estabelecida, recebe mensagens do cliente e as envia de volta para o cliente.

O funcionamento de cada um:

- echo-server.py:

- - O servidor cria um socket TCP (socket.AF_INET, socket.SOCK_STREAM) e o associa ao endereço 127.0.0.1 (localhost) e à porta 65432.
- - Em seguida, ele entra em um loop de escuta (s.listen()) para aguardar por conexões entrantes.
Quando uma conexão é recebida (s.accept()), o servidor aceita a conexão e obtém um novo socket (conn) e o endereço do cliente (addr).
- - Dentro do bloco with conn, o servidor recebe dados do cliente em um loop (conn.recv(1024)), imprime os dados recebidos e, em seguida, envia os dados de volta ao cliente (conn.sendall(data)).

- echo-client.py:

- - O cliente cria um socket TCP (socket.AF_INET, socket.SOCK_STREAM) e se conecta ao endereço 127.0.0.1 (localhost) e à porta 65432.
- - Ele envia a mensagem "Hello, world" ao servidor usando s.sendall(b"Hello, world") e aguarda por uma resposta do servidor usando s.recv(1024).
- - Por fim, o cliente imprime a mensagem recebida do servidor.

Esses códigos implementam um simples sistema de eco, em que o servidor ecoa de volta ao cliente qualquer mensagem que ele envie.

### 4) Analise usando o wireshark explicando os pacotes.

#### Resposta 4:
Wireshark para explicar os pacotes trocados entre o servidor e o cliente durante a comunicação.

#### Preparação:
O servidor está rodando o echo-server.py e o cliente está rodando o echo-client.py.
Ambos estão configurados para se comunicar através do endereço IP 127.0.0.1 (localhost) e a porta 65432.

#### Estabelecimento da Conexão:
- O cliente envia um pacote SYN (synchronize) para iniciar a conexão com o servidor.
- O servidor responde com um pacote SYN-ACK (synchronize-acknowledgement) confirmando a conexão.
- O cliente então envia um pacote ACK (acknowledgement) confirmando a conexão, estabelecendo assim a conexão TCP.

#### Envio de Mensagem:
- O cliente envia um pacote contendo a mensagem "Hello, world" para o servidor.
- O servidor recebe a mensagem e envia um pacote de confirmação (ACK) de volta para o cliente.

#### Recebimento da Mensagem:
- O servidor processa a mensagem recebida e envia um pacote contendo a mensagem de volta para o cliente.
- O cliente recebe a mensagem e confirma o recebimento com um pacote ACK.

#### Encerramento da Conexão:
- Após a troca de mensagens, o cliente envia um pacote FIN (finalize) para encerrar a conexão.
- O servidor responde com um pacote ACK para confirmar o encerramento da conexão.
- O servidor então também envia um pacote FIN para encerrar a conexão do seu lado.
- O cliente responde com um pacote ACK confirmando o encerramento da conexão do lado do servidor.

Essa sequência de pacotes é observada no Wireshark e representa a troca de mensagens entre o servidor e o cliente durante a comunicação TCP. Cada pacote tem um papel específico na estabelecimento, transmissão e encerramento da conexão TCP entre os dois.

#### Print Screem:
[![Print Screm](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/06-Analise-Pacotes.jpg)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/06-Analise-Pacotes.jpg)

### 5) Diferencie a conexão UDP de TCP

#### Resposta 5:

UDP (User Datagram Protocol) e TCP (Transmission Control Protocol) são dois protocolos de transporte usados na Internet.

As principais diferenças entre eles:

- Confiabilidade da conexão: TCP é orientado à conexão, o que significa que estabelece uma conexão antes de enviar dados e garante a entrega ordenada e confiável dos dados. UDP, por outro lado, é não orientado à conexão e não garante a entrega dos dados.

- Controle de fluxo e congestionamento: TCP tem mecanismos embutidos para controle de fluxo e congestionamento, ajustando a taxa de transmissão com base nas condições da rede. UDP não possui esses mecanismos.

- Cabeçalho: Os cabeçalhos de TCP e UDP são diferentes. O cabeçalho TCP é maior, incluindo informações como números de sequência, confirmação, janelas de recebimento e checksum, enquanto o cabeçalho UDP é menor, incluindo apenas informações básicas, como portas de origem e destino e um checksum.

- Exemplos de uso:
    - a) TCP é usado em aplicativos que requerem transferência de dados confiável e ordenada, como navegadores da web, e-mails, transferência de arquivos (FTP) e streaming de vídeo.
    - b) UDP é usado em aplicativos que precisam de baixa latência e podem tolerar perda de dados, como transmissões ao vivo, jogos online e DNS.

##### Um exemplo prático de uso seria o seguinte:

- A pessoa que estiver assistindo a uma transmissão ao vivo, como um jogo de futebol, provavelmente está recebendo os dados através do UDP. Se alguns pacotes de dados forem perdidos no caminho, o sistema não tentará recuperá-los, pois a prioridade é manter a transmissão fluindo em tempo real.

- Por outro lado, se estiver baixando um arquivo grande, como um vídeo, é mais provável que o download seja feito via TCP. Nesse caso, a confiabilidade da entrega é crucial e, se um pacote for perdido, o TCP solicitará que ele seja reenviado para garantir que todos os dados sejam recebidos corretamente.

***

### Simple server UDP:

### 1) Subir o UDP server simple explicar os estados da conexão, bind, listen etc.

#### Resposta 1:

Implementando um servidor UDP simples usando a biblioteca socketserver do Python.

Conceitos envolvidos:

- bind: O método socketserver.UDPServer((HOST, PORT), MyUDPHandler) é usado para associar (bind) o servidor a um endereço IP e porta específicos. Isso permite que o servidor escute (listen) por conexões UDP que chegam nesse endereço e porta.

- listen: No UDP, não há um estado de escuta (listen) como no TCP. O servidor está sempre pronto para receber mensagens, e não precisa esperar por conexões como no TCP.

- handle: O método handle(self) é chamado sempre que o servidor recebe uma mensagem. Ele lida com a mensagem recebida e responde de acordo. Neste caso, ele imprime a mensagem recebida em letras maiúsculas e a envia de volta para o cliente.

- client_address: O endereço do cliente é acessado através de self.client_address. Isso é útil para saber de onde veio a mensagem recebida.

Em resumo, no UDP não há estados de conexão como no TCP. O servidor UDP está sempre pronto para receber mensagens e não mantém uma conexão persistente com os clientes. Ele simplesmente recebe mensagens, processa-as e envia respostas, se necessário. O método bind é usado para associar o servidor a um endereço e porta, mas não há um estado de escuta (listen) no UDP.

### 2) Executar o programa de cliente simple server UDP e verificar os estados da conexão.

#### Resposta 2:

Implementa um cliente UDP simples, não há estados de conexão a serem verificados. Isso ocorre porque o UDP é um protocolo sem conexão, o que significa que não há estabelecimento de conexão, manutenção de estado de conexão ou terminação de conexão como no TCP. Cada mensagem é tratada independentemente e não há garantia de entrega ou ordem das mensagens.

Portanto, não há "estados de conexão" específicos para verificar em um cliente UDP.

### 3) Analise o código fonte

#### Resposta 3:

O código implementa um servidor UDP simples em Python usando a biblioteca socketserver.

- Definição da classe MyUDPHandler: Aqui, estamos definindo uma classe chamada MyUDPHandler que herda de socketserver.BaseRequestHandler. Esta classe é responsável por lidar com as requisições recebidas pelo servidor.

- Comentário de documentação da classe: Um comentário de documentação está incluído para explicar o propósito da classe. Ele menciona que a classe funciona de maneira semelhante à classe de manipulador TCP, mas observa a diferença fundamental de que não há uma conexão e, portanto, o endereço do cliente deve ser explicitamente fornecido ao enviar dados de volta.

- Método handle: Este método é chamado sempre que o servidor recebe uma requisição. Ele extrai os dados recebidos e o socket do cliente da tupla self.request. Em seguida, converte os dados recebidos para maiúsculas, imprime quem enviou a mensagem e o conteúdo da mensagem, e finalmente envia a mensagem de volta ao cliente usando o método sendto() do socket do cliente.

- Bloco de inicialização do servidor: No bloco if __name__ == "__main__":, o código define o endereço IP e a porta em que o servidor UDP será executado (HOST e PORT). Em seguida, cria uma instância de socketserver.UDPServer passando o endereço e a porta, bem como a classe de manipulador MyUDPHandler. O servidor é iniciado chamando serve_forever().

- Uso do bloco "with": O uso do bloco with garante que o servidor seja corretamente encerrado após a execução do bloco, liberando os recursos associados a ele.

Eeste código implementa um servidor UDP simples que escuta as requisições dos clientes, converte os dados recebidos para maiúsculas e os envia de volta ao cliente. Ele usa a classe socketserver.BaseRequestHandler para lidar com as requisições e a classe socketserver.UDPServer para criar e executar o servidor.




***


### Multiserver TCP :

### 1) Subir o tcp server simple explicar os estados da conexão, bind, listen etc.

#### Resposta 1:

O código implementa um servidor TCP multithreaded capaz de lidar com múltiplos clientes simultaneamente, utilizando a classe socketserver.ThreadingTCPServer do módulo socketserver do Python.

##### Bind (associação):
- A linha server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler) cria uma instância do servidor TCP multithreaded.
- O método ThreadingTCPServer é usado para associar (bind) o endereço HOST (neste caso, "localhost") e a porta PORT (65432) ao servidor.
- Essa operação é essencialmente o processo de "amarrar" o servidor a um endereço e porta específicos, para que ele possa aceitar conexões de entrada nesse endereço e porta.

##### Listen (escuta):
- Após o bind, a linha server.serve_forever() ativa o servidor.
- Dentro do método serve_forever(), a implementação subjacente do servidor entra em um loop para aguardar e manipular conexões entrantes.
- Durante este tempo, o servidor está "ouvindo" (listen) na porta especificada (PORT) por conexões entrantes.

##### Estado da conexão:
- O servidor está constantemente em um estado de escuta (listen) por novas conexões.
- Quando uma conexão é estabelecida, o servidor cria uma nova thread para lidar com essa conexão, permitindo que o servidor continue a ouvir por novas conexões enquanto atende aos clientes existentes.

Este servidor TCP multithreaded é capaz de aceitar conexões de múltiplos clientes simultaneamente, mantendo um estado de escuta constante para novas conexões e associando essas conexões aos threads de tratamento correspondentes.

### 2) Executar o programa de cliente simple server tcp e verificar os estados da conexão. ()

#### Resposta 2:
Mesmo resultado da pergunta 2 logo acima. 👆

Entretanto, fiz a execução do Client UDP Simple (Client-UDP-Simple.py) e tive o seguinte resultado:

#### Print Screem:
[![Print Screm](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/05-Mensage-UDP.jpg)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/05-Mensage-UDP.jpg)

### 3) Analise o código fonte

#### Resposta 3:

O código Python implementa um servidor TCP simples que aceita conexões de clientes, recebe mensagens dos clientes, imprime essas mensagens no console e envia de volta para os clientes.

##### Analise de cada parte do código de forma didática:

##### Importação de Módulos:
- Import socket: Importa o módulo socket para lidar com comunicação em rede.

##### Definição do Endereço e Porta:
- HOST = "127.0.0.1": Define o endereço IP padrão de loopback (localhost).
- PORT = 65432: Define a porta na qual o servidor irá escutar por conexões.

##### Criação do Socket do Servidor:
- with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:: Cria um novo socket TCP (socket.SOCK_STREAM) usando o endereço IPv4 (socket.AF_INET). O socket é atribuído à variável s.

##### Bind (Associação):
- s.bind((HOST, PORT)): Associa o socket a um endereço e porta específicos. Neste caso, o endereço é HOST e a porta é PORT.

##### Listen (Escuta):
- s.listen(): Coloca o socket em modo de escuta, permitindo que ele aceite conexões entrantes.

##### Aceitação de Conexões:
- conn, addr = s.accept(): Aceita uma nova conexão de cliente. O método accept() bloqueia a execução do código até que uma conexão seja estabelecida.
- conn é um novo socket que representa a conexão com o cliente.
- addr é uma tupla contendo o endereço IP e o número da porta do cliente.

##### Comunicação com o Cliente:
- with conn:: Define um bloco de código que será executado enquanto a conexão estiver ativa.
- data = conn.recv(1024): Recebe dados do cliente. O argumento 1024 especifica o número máximo de bytes a serem recebidos de uma vez.
- print(str(data)): Imprime os dados recebidos do cliente no console.
- conn.sendall(data): Envia de volta para o cliente os dados recebidos. Neste caso, o - servidor simplesmente ecoa as mensagens de volta para o cliente.

Esse código forma a base de um servidor TCP simples que pode ser usado para comunicação em rede

### 4) Analise usando o wireshark explicando os pacotes.

#### Resposta 4:
Wireshark para explicar os pacotes trocados entre o servidor e o cliente durante a comunicação.

#### Preparação:
O servidor está rodando o echo-server.py e o cliente está rodando o echo-client.py.
Ambos estão configurados para se comunicar através do endereço IP 127.0.0.1 (localhost) e a porta 65432.

#### Estabelecimento da Conexão:
- O cliente envia um pacote SYN (synchronize) para iniciar a conexão com o servidor.
- O servidor responde com um pacote SYN-ACK (synchronize-acknowledgement) confirmando a conexão.
- O cliente então envia um pacote ACK (acknowledgement) confirmando a conexão, estabelecendo assim a conexão TCP.

#### Envio de Mensagem:
- O cliente envia um pacote contendo a mensagem "Hello, world" para o servidor.
- O servidor recebe a mensagem e envia um pacote de confirmação (ACK) de volta para o cliente.

#### Recebimento da Mensagem:
- O servidor processa a mensagem recebida e envia um pacote contendo a mensagem de volta para o cliente.
- O cliente recebe a mensagem e confirma o recebimento com um pacote ACK.

#### Encerramento da Conexão:
- Após a troca de mensagens, o cliente envia um pacote FIN (finalize) para encerrar a conexão.
- O servidor responde com um pacote ACK para confirmar o encerramento da conexão.
- O servidor então também envia um pacote FIN para encerrar a conexão do seu lado.
- O cliente responde com um pacote ACK confirmando o encerramento da conexão do lado do servidor.

Essa sequência de pacotes é observada no Wireshark e representa a troca de mensagens entre o servidor e o cliente durante a comunicação TCP. Cada pacote tem um papel específico na estabelecimento, transmissão e encerramento da conexão TCP entre os dois.

#### Print Screem:
[![Print Screm](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/06-Analise-Pacotes.jpg)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/06-Analise-Pacotes.jpg)

### 5) Explique as diferenças de multi conexões e porque a cada conexão a porta "muda". Demonstre a mudança de porta usando o Wireshark

#### Resposta 5:
Em um servidor TCP, a porta do servidor (neste caso, 65432) permanece a mesma para todas as conexões. A porta de origem do cliente é que muda a cada nova conexão. Isso ocorre porque cada conexão TCP é identificada por um conjunto único de endereço IP e porta de origem e destino. O servidor mantém a mesma porta para ouvir por novas conexões, enquanto as portas de origem dos clientes variam para distinguir entre as diferentes conexões.

##### Print Screem 1:
[![Print Screm](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/05-Mensage-UDP-2.jpg)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/05-Mensage-UDP-2.jpg)

##### Print Screem 2:
[![Print Screm](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/05-Mensage-UDP-Wireshark.jpg)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/05-Mensage-UDP-Wireshark.jpg)




Extra:

#### Resposta 3 extra: netstat e grep:

Executando o comando "netstat -an | grep "65432" lista todas as conexões de rede e as estatísticas de conexão do sistema. O pipe (|) redireciona a saída desse comando para o comando grep "65432", que filtra as linhas que contenham o número da porta "65432". 

O comando completo retorna informações sobre as conexões de rede que estão utilizando a porta "65432" no sistema.

#### Print Screem:
[![Print Screm](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/03-Netstat_Grep.jpg)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/03-Netstat_Grep.jpg)

#### Resposta 3 extra: nmap:

O comando "nmap -p65432 localhost" executa uma varredura de portas na máquina local (localhost) para verificar se a porta 65432 está aberta. O nmap é uma ferramenta de segurança e auditoria de rede que mostra quais portas estão abertas em um sistema, ajudando a identificar possíveis vulnerabilidades.

#### Print Screem:
[![Print Screm](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/03.1-Nmap.jpg)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/03.1-Nmap.jpg)






Thank you, teacher! 😎

##

#### Bônus! :P

[![Print Screm](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/artur-e-gustavo.jpg)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/artur-e-gustavo.jpg)



