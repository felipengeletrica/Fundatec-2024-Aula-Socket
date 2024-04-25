1.Simple server TCP:
Estado da conexão TCP: O TCP possui três estados principais de conexão: SYN (sincronização), SYN-ACK (sincronização-acknowledgement) e ACK (acknowledgement), formando o handshake TCP.
Bind: Associa um socket a um endereço IP e porta.
Listen: Coloca o socket TCP no estado de escuta, esperando por conexões entrantes.
Accept: Aceita uma conexão entrante e cria um novo socket para comunicação com o cliente.

2.Diferença entre conexão UDP e TCP:
TCP (Transmission Control Protocol):
Orientado à conexão: estabelece uma conexão antes da transferência de dados.
Confiável: garante a entrega ordenada dos dados e retransmite pacotes perdidos.
Bidirecional: suporta comunicação em ambas as direções simultaneamente.
Overhead maior devido ao controle de fluxo, controle de congestionamento e retransmissões.
UDP (User Datagram Protocol):
Não orientado à conexão: não estabelece uma conexão prévia.
Não confiável: não garante a entrega ou a ordem dos pacotes.
Menor overhead: mais rápido e eficiente para aplicações que toleram perda de dados.
Suporta multicasting e broadcasting.
![Print1](/Screenshots/PRINT1.png)
3.Quando um servidor recebe várias conexões, cada uma dessas conexões é identificada por uma combinação única de endereço IP e número de porta. A porta é usada para distinguir entre diferentes conexões de rede no mesmo computador.
![Print2](/Screenshots/PRINT2.png)
![Print3](/Screenshots/PRINT3.png)
![Print4](/Screenshots/PRINT4.png)
![Print5](/Screenshots/PRINT5.png)

