# Trabalho socket

Estes sockets fazem parte das aulas de redes de computadores!
Enjoy meus alunos!

Alunos!!!
***
## Sobre o trabalho

Documente com print e coloque aqui as respostas

### Simple server TCP :

1) Subir o tcp server simple explicar os estados da conexão, bind, listen etc.

2) Executar o programa de cliente simple server tcp e verificar os estados da conexão.

3) Analise o código fonte

4) Analise usando o wireshark explicando os pacotes.

5) Diferencie a conexão UDP de TCP
***

### Simple server UDP :

1) Subir o tcp server simple explicar os estados da conexão, bind, listen etc.

2) Executar o programa de cliente simple server tcp e verificar os estados da conexão.

3) Analise o código fonte

4) Analise usando o wireshark explicando os pacotes.

***

### Multiserver TCP :

1) Subir o tcp server simple explicar os estados da conexão, bind, listen etc.

2) Executar o programa de cliente simple server tcp e verificar os estados da conexão.

3) Analise o código fonte

4) Analise usando o wireshark explicando os pacotes.

5) Explique as diferenças de multi conexões e porque a cada conexão a porta "muda". Demonstre a mudança de porta usando o Wireshark

***
### Conexão com máquina remota do colega :

1) Subir o tcp server na máquina do colega, verificar o IP da máquina (certifique que ele esteja na mesma rede que você)

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



