# Modelo Requisição e Resposta

Normalmente enquanto navegamos em um site, estamos constantemente enviando requisições ao servidor, que está localizado o site, e recebendo as respostas através do nosso navegador. Porém o **servidor não armazena as requisições anteriores**.

Naturalmente podemos pensar que, então se o servidor não armazena as informações de requisições anteriores feitas por mim, como fica os sites em que faço login e ele utiliza essa informação para acesso em áreas restritas a usuários cadastrados, por exemplo?

Isso é possível através de um **identificador emitido pelo servidor**, cada vez que você realiza o login. Esse identificador **é enviado ao navegador com a instrução que ele deve armazenar essa informação e, a cada nova requisição, enviar essa informação junto para o servidor.**

Isso só permitido graças ao conceito de sessão, uma sessão HTTP nada mais é que um tempo que o cliente permanece ativo no sistema!

E para que a sessão seja viabilizada utiliza-se **cookies** que são armazenados no navegador, que guardam informações pertinentes que são enviadas ao servidor a cada requisição, um exemplo é o **JSESSIONID**, utilizado para cifrado um ID de acesso que só é reconhecido e decifrado pelo servidor.

## Cookies

Um cookie é um pequeno arquivo de texto, normalmente criado pela aplicação web, para guardar algumas informações sobre usuário no navegador. Quais são essas informações depende um pouco da aplicação.

Pode ser que fique gravado alguma preferência do usuário. Ou algumas informações sobre as compras na loja virtual ou, como vimos no vídeo, a identificação do usuário. Isso depende da utilidade para a aplicação web.

Um cookie pode ser manipulado e até apagado pelo navegador e, quando for salvo no navegador, fica associado com um domínio. Ou seja, podemos ter um cookie para `www.alura.com.br`, e outro para `www.caelum.com.br`. Aliás, um site ou web app pode ter vários cookies!