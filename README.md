# Trabalho Socket - Redes de Computadores


#### Aluno: Diogo Oliveira
#### Turma: TI23

***

### Simple server TCP:



![Screenshot (46)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/assets/112041509/e743c957-e7b7-432a-9006-9fb2f0d95878)



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

***

### Simple server UDP :

![Screenshot (47)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/assets/112041509/df872649-cfca-47dc-8d90-e5254d958166)


***

### Multiserver TCP:

![Screenshot (48)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/assets/112041509/61fd9236-bca1-488a-b7a9-899cef02f4d8)

### 1. Explique as diferenças de multi conexões e porque a cada conexão a porta "muda". Demonstre a mudança de porta usando o Wireshark

#### Multiplas Conexões:
Em um servidor que suporta múltiplas conexões, o servidor é capaz de atender a solicitações de vários clientes simultaneamente. Isso é importante em muitos casos, especialmente em ambientes de rede onde há múltiplos clientes que precisam interagir com o servidor ao mesmo tempo.
No contexto de um servidor TCP, cada nova conexão é tratada separadamente por uma nova instância do manipulador de solicitações, permitindo que o servidor atenda a várias conexões ao mesmo tempo.

#### Porta "muda" a Cada Conexão:
Quando um servidor TCP aceita uma nova conexão de um cliente, uma nova porta é atribuída para essa conexão específica. Isso acontece para permitir que o servidor diferencie entre várias conexões ativas.
A combinação de endereço IP do servidor e porta de destino única para cada conexão garante que os pacotes de dados sejam roteados corretamente entre o cliente e o servidor, mesmo quando há várias conexões simultâneas.
A porta de origem do cliente também pode variar, mas isso é gerenciado pelo próprio cliente e não afeta diretamente o servidor. Cada conexão do cliente será representada por uma combinação única de endereço IP e porta de origem.

***
### Conexão com máquina remota com o Vitor Alicer:

![Captura de Tela (19)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/assets/112041509/a4ebfa34-8ed5-4d91-bfa3-c6298af8a831)

***

### WireShark
![Captura de Tela (20)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/assets/112041509/5bf95972-52ff-49bd-b734-dd3a744a0711)




