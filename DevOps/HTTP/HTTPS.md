# HTTPS

Qualquer operação realizada pelo usuário no navegador, envia requisições para o servidor, esse caminho possui N intermediários, o roteador, o modem, o provedor etc.

Portanto, determinados casos como acesso ao _internetbanking_ por exemplo, que possuem informações sensíveis, precisariam de uma maior proteção das informações que são passadas do navegador até o servidor da aplicação, sem que os intermediários conseguissem acessar essas informações.

Para isso surge o **HTTPS**, que além do protocolo padrão HTTP, ele possui mais uma camada de segurança, chamada **SSL/TLS** (_Secure Sockets Layer / Transport Layer Security_).

Sem essa camada de segurança, nossos dados são enviados pelos requisitos, em texto puro, podendo ser visualizado facilmente por qualquer intermediário.

Para que o navegador possua o protocolo de segurança é necessário que tenha uma **identidade**, através dessa identidade é emitido um **certificado digital** com uma chave pública que será usada para criptografar os dados enviados através dos requisitos.

Quando o requisito chega ao servidor, ele terá uma chave privada que somente ela possui para conseguir descriptografar os dados do requisito

Em suma o site que deseja possuir essa camada de segurança a mais precisa buscar uma autoridade certificadora, para que seja emitido um certificado digital e uma chave pública que aplicará a camada de segurança

O HTTPS utiliza uma chave pública e uma chave privada para a cifrar e decifrar a comunicação entre navegador e servidor. Essas chaves estão ligadas matematicamente, o que foi cifrado pela chave pública (navegador) só pode ser decifrado pela chave privada (servidor). Por serem duas chaves **diferentes** envolvidas, a criptografia é chamada de **criptografia assimétrica,** no entanto essa forma é **lenta**.

Por outro lado temos a criptografia simétrica, que usa a mesma chave para cifrar e decifrar os dados. Essa por sua vez é muito **mais rápida**, mas **não é tão segura**. Como existe apenas uma chave, ela fica espalhada pelos clientes (navegadores) e qualquer um, que tem a posse dessa chave, pode decifrar a comunicação.

Para resolver esse problema o **HTTPS utiliza ambos os métodos de criptografia, assimétrica e simétrica.** No certificado vem a chave pública para o cliente e o servidor continua com a chave privada, por isso ser lento o **cliente gera uma chave simétrica ao vivo**, uma chave que só o cliente e o servidor com o qual está se comunicando naquele momento. Essa chave exclusiva (simétrica) é então enviada para o servidor utilizando a criptografia assimétrica (chave privada e pública) e então é utilizada para o restante da comunicação, por ser mais rápida.

Portanto o HTTPS **começa** com a criptografia **assimétrica** para **depois** mudar para criptografia **simétrica**. Essa chave simétrica gerada é reaproveitada nas requisições seguintes.