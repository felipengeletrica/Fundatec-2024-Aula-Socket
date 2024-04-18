Diferença entre conexão UDP de TCP - O TCP é como enviar uma carta registrada. Você tem garantia de que a carta chegará ao destino, e se não chegar, você será informado. Além disso, as cartas chegam na ordem em que foram enviadas.
Já o UDP é como enviar um bilhete pelo vento. Você o joga e torce para que chegue ao destino, mas não tem certeza. Além disso, pode chegar fora de ordem, e às vezes nem chegar.
Basicamente, o TCP é mais confiável e garante a entrega correta e ordenada dos dados, enquanto o UDP é mais rápido e leve, mas não oferece garantias sobre a entrega ou ordem dos pacotes.


Explique as diferenças de multi conexões e porque cada conexão a porta "muda". Demonstre a mudança de porta usando o Wireshark) 
Quando múltiplas conexões estão acontecendo ao mesmo tempo, cada uma precisa de uma identificação única, chamada de porta, para enviar e receber dados corretamente. As portas mudam para garantir que cada nova conexão tenha sua própria linha, evitando confusão. No Wireshark, você vê essa mudança como diferentes números de porta de destino nos pacotes de dados, assim como diferentes chamadas entrantes chegando em linhas telefônicas distintas.


![redes CAPTURA1](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/assets/130008750/4551aeb5-d8ef-4b8e-8825-5a63e16cd1a5)

![redes CAPTURA2](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/assets/130008750/71e945b5-f632-4911-a3d2-4e2f7988103d)

![redes CAPTURA3](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/assets/130008750/f4a6f086-ef8a-4136-98fd-bbf48db4a7de)

![Capturar porta](https://github.com/felipengeletrica/Fundatec-2024-Aula-Socket/assets/130008750/fd65d857-9697-49e9-8934-3cf7920a0207)
