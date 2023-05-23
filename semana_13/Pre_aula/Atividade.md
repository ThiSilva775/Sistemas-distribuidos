Curso de Engenharia de Software - UniEVANGÉLICA 
Disciplina de Sistemas Distribuidos 
Dev: Thiago Silva Soares
DATA: 23/05/2023

Quando falamos em sincronização de sockets, estamos nos referindo ao processo de coordenação e controle da comunicação entre dois ou mais pontos de extremidade em uma rede por meio de sockets. Um socket é uma interface de programação que permite a comunicação entre processos em diferentes computadores ou dentro do mesmo computador.

Existem dois principais modelos de comunicação utilizados na sincronização de sockets: o modelo cliente-servidor e o modelo peer-to-peer.

Modelo Cliente-Servidor:
Nesse modelo, a comunicação é estabelecida entre um cliente e um servidor. 

O cliente é o ponto de extremidade que inicia a comunicação, enquanto o servidor é o ponto de extremidade que espera por solicitações de clientes e responde a elas. 

O cliente envia uma solicitação ao servidor e aguarda por uma resposta. Durante esse tempo de espera, o cliente pode ficar bloqueado até que a resposta seja recebida. 

Esse tipo de sincronização é conhecido como sincronização bloqueante ou síncrona. 

Quando o servidor recebe a solicitação, ele a processa e envia uma resposta de volta ao cliente. 

Esse modelo é amplamente utilizado em aplicações em que há uma divisão clara entre os papéis de cliente e servidor, como aplicações web, onde os navegadores atuam como clientes e os servidores fornecem os recursos solicitados.

Modelo Peer-to-Peer:
Nesse modelo, não há uma distinção clara entre cliente e servidor. 

Os pontos de extremidade, chamados de pares (peers), agem tanto como clientes quanto como servidores. 

Cada par pode enviar e receber dados, bem como iniciar e responder a solicitações. 

A comunicação ocorre diretamente entre os pares sem a necessidade de um servidor centralizado. 

Nesse modelo, a sincronização de sockets pode ser implementada de diferentes maneiras. 

Por exemplo, pode-se adotar um mecanismo de troca de mensagens assíncrono, em que os pares podem enviar mensagens uns aos outros sem esperar uma resposta imediata. 

Alternativamente, pode-se usar um esquema de bloqueio não síncrono, em que os pares podem enviar mensagens e continuar suas operações sem aguardar uma resposta imediata. 

O modelo peer-to-peer é comumente utilizado em sistemas de compartilhamento de arquivos, jogos multiplayer e aplicações de comunicação em tempo real, como chamadas de vídeo ponto a ponto.

Esses são os dois principais modelos de comunicação utilizados na sincronização de sockets. 

A escolha do modelo adequado depende dos requisitos específicos da aplicação e da natureza da comunicação que se deseja estabelecer.