#Trabalho socket

Estes sockets fazem parte das aulas de redes de computadores! Enjoy meus alunos!


#Sobre o trabalho

#Documente com print e coloque aqui as respostas 
***
##Simple server TCP :

#####Subir o tcp server simple explicar os estados da conexão, bind, listen etc.
    Com o comando python3 Server-TCP-simple.py o programa inicia e lança duas mensagens 1) Bind (Vinculando) indicando a conexão entre um soquet e um endereço. Conforme o codigo em Python o endereço é do loopback 127.0.0.1 e a porta 65432 estas duas informações vão permanecer vinculadas.
    Em seguida o servidor envia uma msg indicando que ele esta escutando a porta, aguardando alguma mensagem direcionada para a porta. Isso é representado pela mensagem na tela de Listen (Escutando).
    
#####Executar o programa de cliente simple server tcp e verificar os estados da conexão.
    Ao executar no terminal o cliente TCP ele envia uma msg para o servidor que imprimi na tela as informações pertinentes a conexão tais como o ip do Cliente e a porta de comunicação. Além disso o servidor imprime a mensagem proveniente do cliente e na sequência dá um retorno ao cliente indicando que a mensagem foi ao servidor e retornou ao cliente indicando o sucesso da 'conversa' entre o cliente e o servidor. Por fim o servidor encerra a operação.
    
    Analise o código fonte
    
    Analise usando o wireshark explicando os pacotes.
    Diferencie a conexão UDP de TCP
***
##Simple server UDP :

#####Subir o tcp server simple explicar os estados da conexão, bind, listen etc.
#####Executar o programa de cliente simple server tcp e verificar os estados da conexão.
#####Analise o código fonte
#####Analise usando o wireshark explicando os pacotes.
***
##Multiserver TCP :
#####Subir o tcp server simple explicar os estados da conexão, bind, listen etc.
#####Executar o programa de cliente simple server tcp e verificar os estados da conexão.
#####Analise o código fonte
#####Analise usando o wireshark explicando os pacotes.
#####Explique as diferenças de multi conexões e porque a cada conexão a porta "muda". Demonstre a mudança de porta usando o Wireshark

