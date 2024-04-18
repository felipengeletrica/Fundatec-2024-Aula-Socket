# Trabalho Socket - Redes de Computadores


#### Aluno: Diogo Oliveira
#### Turma: TI23

***

### Simple server TCP:


![Screenshot (45)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/assets/112041509/8d39b33a-087b-464e-a502-885dcc4fc95b)



#### 1. Bind
Bind é o processo de associar um endereço IP e um número de porta a um socket. No contexto do servidor, isso significa que o servidor está especificando em qual interface de rede e porta ele estará escutando por conexões entrantes.
Na linha 11, o s.bind((HOST, PORT)) associa o endereço IP HOST e o número de porta PORT ao socket s, permitindo que o servidor escute por conexões nesse endereço e porta específicos.

#### 2. Listen
Após o bind, o socket do servidor precisa ser colocado em modo de escuta para aceitar conexões entrantes dos clientes.
A função listen() é usada para colocar o socket em estado de escuta. Ela define o número máximo de conexões pendentes que o socket pode ter.
No código, a linha s.listen() coloca o socket em modo de escuta, permitindo que ele aceite conexões entrantes.

#### 3. Connected

Quando um cliente se conecta com sucesso a um servidor, o servidor entra no estado de "conectado".
Na linha 20, o conn, addr = s.accept() aceita uma conexão entrante de um cliente. O método accept() bloqueia a execução até que uma nova conexão seja recebida.
Após essa linha, o servidor imprime "Connected", indicando que uma conexão foi estabelecida com sucesso.

#### 4. Qual a diferença entre a conexão UDP de TCP?

O TCP cria uma linha de comunicação segura para garantir a transmissão confiável de todos os dados. Uma vez que uma mensagem é enviada, o recebimento é verificado para garantir que todos os dados foram transferidos.

O UDP não estabelece uma conexão ao enviar dados. Ele envia os dados sem confirmação de recebimento ou verificação de erros. Isso significa que alguns ou todos os dados podem ser perdidos durante a transmissão.

A principal diferença entre TCP (protocolo de controle de transmissão) e UDP (protocolo de datagramas do usuário) é que TCP é um protocolo baseado em conexão e UDP é sem conexão. Enquanto o TCP é mais confiável, ele transfere dados mais lentamente. O UDP é menos confiável, mas funciona mais rapidamente.
