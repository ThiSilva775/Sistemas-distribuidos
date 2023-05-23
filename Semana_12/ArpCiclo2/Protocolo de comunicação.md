Curso de Engenharia de Software - UniEVANGÉLICA 
Disciplina de Sistemas Distribuidos 
Dev: Thiago Silva Soares
DATA: 23/05/2023

O protocolo de comunicação será baseado em TCP e consistirá em mensagens de texto simples, cada uma começando com um cabeçalho indicando o tipo e o tamanho da mensagem.

O servidor aguardará as mensagens dos clientes e processará cada mensagem de acordo com o tipo de mensagem.

O tipo de mensagem será:

LOGIN: Mensagem enviada pelo cliente para se autenticar no servidor. O corpo do e-mail conterá o nome de usuário e a senha em texto simples.

LOGOUT: A mensagem enviada pelo cliente para se desconectar do servidor.

SEND_MESSAGE: Uma mensagem enviada pelo cliente, enviando a mensagem para um destinatário específico. O corpo da mensagem conterá o nome do destinatário e o conteúdo da mensagem.

BROADCAST: envio de mensagem, o cliente envia uma mensagem para todos os usuários conectados. O corpo da mensagem conterá o conteúdo da mensagem.

RECEIVE_MESSAGE: mensagem enviada pelo servidor para um cliente para informar que uma nova mensagem foi recebida. O corpo da mensagem conterá o nome do remetente e o conteúdo da mensagem.


ERROR: mensagem enviada pelo servidor para informar que ocorreu um erro. O corpo da mensagem conterá uma descrição do erro.


Formato das mensagens:


Cada mensagem terá o seguinte formato:


|------------------|------------------|------------------|


Tipo (8 bytes)	Comprimento (8)	Corpo da mensagem


O campo "Tipo" terá o valor de um dos tipos de mensagem definidos acima. O campo "Comprimento" indicará o tamanho do corpo da mensagem em bytes. O campo "Corpo da mensagem" conterá os dados da mensagem.
