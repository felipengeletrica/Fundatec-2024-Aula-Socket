# TRABALHO SOCKET 

Trabalho Sockets que faz parte da aula de Redes.

#### Aluno: Artur Bazzanella Christmann
#### Professor: Felipe Vargas
#### Turma: TI23

#

### Sobre o trabalho

Documente com print e coloque aqui as respostas

### Simple server TCP :

### 1) Subir o tcp server simple explicar os estados da conexão, bind, listen etc.

#### Resposta 1:

Ao subir o Servidor Simples com o comando "python Server-TCP-simple.py", que é executado através de um script em Python, o serviço primitivo de transporte de soquetes TCP é iniciado. Isso envolve os seguintes estados da conexão:

Bind: O servidor associa um endereço local (por exemplo, um endereço IP ou DNS, neste caso "localhost", e um número de porta, que neste script é a porta 65432) ao soquete.

Listen: O servidor fica pronto para receber conexões entrantes, anunciando a disponibilidade para conexão e especificando o tamanho da fila de conexões pendentes.

Com isso, o servidor está pronto para estabelecer conexões ativas, enviar e receber dados através delas.

[![Print Screm](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/01-Start-PY-Server.jpg)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/01-Start-PY-Server.jpg)

### 2) Executar o programa de cliente simple server tcp e verificar os estados da conexão.

#### Resposta 2:

Neste script, que é executado via "localhost" (127.0.0.1) na porta "65432", envia uma mensagem de teste ("Hello, world!").

As quatro primeiras primitivas na lista são executadas pelos servidores nessa ordem: a primitiva SOCKET cria um novo ponto final e aloca espaço de tabela para ele na entidade de transporte.

Os parâmetros da chamada especificam o formato de endereçamento a ser usado, o tipo de serviço desejado (por exemplo, um fluxo de bytes confiável) e o protocolo.

Uma chamada SOCKET bem-sucedida retorna um descritor de arquivo comum que será usado nas chamadas subsequentes, exatamente como uma chamada OPEN.

Apresentando na tela o valor recebido "Hello, world".

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

Executando o comando "netstat -an | gep "65432" lista todas as conexões de rede e as estatísticas de conexão do sistema. O pipe (|) redireciona a saída desse comando para o comando grep "65432", que filtra as linhas que contenham o número da porta "65432". 

O comando completo retorna informações sobre as conexões de rede que estão utilizando a porta "65432" no sistema.

[![Print Screm](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/03-Netstat_Grep.jpg)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/03-Netstat_Grep.jpg)

#### Resposta 3 extra - nmap:

[![Print Screm](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/03.1-Nmap.jpg)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/03.1-Nmap.jpg)

### 4) Analise usando o wireshark explicando os pacotes.

#### Resposta 4:
EM DESENVOLVIMENTO!

### 5) EXTRAS: Servidor UDP and Mensages.

#### Resposta 5.1:
[![Print Screm](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/04-Start-PY-Server-UDP.jpg)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/04-Start-PY-Server-UDP.jpg)

#### Resposta 5.2:
[![Print Screm](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/05-Mensage-UDP.jpg)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/05-Mensage-UDP.jpg)


***

### Multiserver TCP :

### 1) Subir o tcp server simple explicar os estados da conexão, bind, listen etc.

#### Resposta 1:
EM DESENVOLVIMENTO!


### 2) Executar o programa de cliente simple server tcp e verificar os estados da conexão.

#### Resposta 2:
EM DESENVOLVIMENTO!

### 3) Analise o código fonte

#### Resposta 3:
EM DESENVOLVIMENTO!

### 4) Analise usando o wireshark explicando os pacotes.

#### Resposta 4:
EM DESENVOLVIMENTO!

### 5) Explique as diferenças de multi conexões e porque a cada conexão a porta "muda". Demonstre a mudança de porta usando o Wireshark

#### Resposta 5:
EM DESENVOLVIMENTO!

Thank you, teacher! 😎

##

#### Bônus! :P

[![Print Screm](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/artur-e-gustavo.jpg)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/blob/Trabalho_Artur/Trabalho_Artur/artur-e-gustavo.jpg)



