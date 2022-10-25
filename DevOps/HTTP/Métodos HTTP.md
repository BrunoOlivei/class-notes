# Métodos HTTP

As requisições possuem **métodos** que indicam uma ação a ser realizada pelo servidor.

As principais são `GET` e `POST`

GET é utilizado quando desejamos receber uma informação do servidor, as informações relevantes ficam postas na URL. Um exemplo disso é quando realizamos uma pesquisa no YouTube por exemplo, percebemos que a URL é alterada, contendo os termos que pesquisamos:

[](https://www.youtube.com/results?search_query=python)[https://www.youtube.com/results?search_query=python](https://www.youtube.com/results?search_query=python)

Já o POST é utilizado para passar informações ao servidor no corpo da requisição, ou seja dessa forma não fica visível na URL, muito utilizada também para realizar um login em uma página.

Existem outros métodos como o `DELETE` e o `PUT` que servem para deletar algum recurso e alterar respectivamente.

Analisando a URL do YouTube, temos após o domínio o **recurso** `results` o ponto de interrogação é utilizado para sinalizar um parâmetro que no caso é `search_query=python` onde search_query é o nome do parâmetro e python é o valor do parâmetro. Pares de nome e valor são sempre separados por um sinal de igual (=).

Podemos concatenar outros parâmetros, para isso basta adicionar um "e" comercial (&) entre os pares nome do parâmetro e valor do parâmetro.