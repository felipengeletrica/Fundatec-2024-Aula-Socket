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
![Captura de Tela (4)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/assets/130003743/b18ec754-acb8-4606-a775-59665155ef0a)

3.Quando um servidor recebe várias conexões, cada uma dessas conexões é identificada por uma combinação única de endereço IP e número de porta. A porta é usada para distinguir entre diferentes conexões de rede no mesmo computador.

![Captura de Tela (1)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/assets/130003743/16308d35-1d7f-4d68-b93e-ebd4d250aec9)
![Captura de Tela (2)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/assets/130003743/2a7706f8-f9d4-4864-994e-aea5f61c9ed9)
![Captura de Tela (3)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/assets/130003743/f13c2335-39eb-4349-b061-5fb49a83b8a5)
![Captura de Tela (5)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/assets/130003743/48fef3fa-7746-4252-9db4-dcf0b7b54e9f)

