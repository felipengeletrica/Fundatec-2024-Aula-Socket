- Simple server TCP  

Diferencie a conexão UDP de TCP: 

TCP: É uma conexão orientada a conexões, o que significa que é altamente confiável. Ele garante que os dados sejam entregues na ordem correta e sem erros, retransmitindo pacotes perdidos e controlando o fluxo de dados para evitar congestionamentos na rede.

UDP: É uma conexão não orientada a conexões e não confiável. Ele não garante a entrega dos dados nem a ordem em que são entregues. Os pacotes podem ser perdidos, duplicados ou entregues fora de ordem.

- Multiserver TCP 

Explique as diferenças de multi conexões e porque a cada conexão a porta "muda". Demonstre a mudança de porta usando o Wireshark:

TCP (Transmission Control Protocol):

No TCP, cada conexão é única e é identificada por um conjunto de endereços IP de origem e destino, bem como números de porta de origem e destino.

Para estabelecer uma conexão TCP, é necessário um processo de três vias de handshake, durante o qual um número de porta efêmero (temporário) é atribuído para essa conexão.

O TCP é uma conexão orientada, garantindo que os dados sejam entregues na ordem correta e sem erros. Portanto, ele mantém o estado da conexão e associa uma porta efêmera para cada conexão.

UDP (User Datagram Protocol):

No UDP, as conexões não são mantidas e não há estabelecimento de conexão antes da transmissão de dados.
Cada pacote UDP é independente e não possui um estado associado. Portanto, não há necessidade de uma porta efêmera para manter o estado da conexão.

![Captura de Tela (1)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/assets/130003783/175b8fb7-70c5-423a-b9f3-6c634a58b7f2)
![Captura de Tela (2)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/assets/130003783/38cab880-445a-48c5-ab53-cf70df2ae6b4)
![Captura de Tela (3)](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/assets/130003783/3886e64c-f103-42a2-8121-a3cf8651987d)

![xd](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/assets/130003783/86abcc0e-3a39-48c0-9745-81f2e56b08d6)

![w1](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/assets/130003783/edabe01c-fe7d-4a05-bec6-33c39fa705bd)



