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

3.Quando um servidor recebe várias conexões, cada uma dessas conexões é identificada por uma combinação única de endereço IP e número de porta. A porta é usada para distinguir entre diferentes conexões de rede no mesmo computador.

![Captura de Tela (1)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/assets/130003743/16308d35-1d7f-4d68-b93e-ebd4d250aec9)
![Captura de Tela (2)](https://github.com/felipengeletrica/Fundatec-2![Captura de Tela (3)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/assets/130003743/d763de15-e145-4d52-9326-a4165a9dadec)
024-Aula-Socket/assets/130003743/3bfbb2cb-d3bb-4206-a8ad-1ed509a21920)
