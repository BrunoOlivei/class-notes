# Entendendo uma URL

http://www.alura.com.br

Tome como exemplo o site da Alura, o HTTP refere-se ao protocolo utilizado para comunicação entre o navegador e o servidor, assim como o HTTPS.

Já a parte `com` e `br` são a **raiz** do domínio, sendo a primeira indicando uma página comercial e a segunda indicando o país de origem da URL. 

Existem outros tipos de raiz que podem ser encontrados como por exemplo `org` para páginas de organizações governamentais ou não, também temos `net` `app` `io` e muitas outras.

Utilizando o `br` temos os sub-domínios como o `com`, `gov`, `edu`, e muitos outros, por fim, como parte do sub-domínio temos o nome como Alura, Caelum, G1, etc.

## Por baixo dos panos

Por baixo dos panos quando digitamos um domínio no nosso navegador e apertamos o `enter` estamos enviando para o **DNS - Domain Name System,** que basicamente é um grande banco de dados que contém os domínios registrados. 

Ao receber a **URL** o DNS busca em seu banco de dados e retorna um **endereço IP,** que é representado por números separados por pontos, (172.217.29.68) este endereço IP é o endereço do servidor onde se encontra a aplicação que deseja acessar, nesse caso o Google.

Mas por que todo esse caminho? 

Pois é através desses conjuntos de números e pontos que as máquinas se reconhecem e se encontram, como é muito mais difícil para um humano memorizar esses conjuntos, criou-se os domínios como estamos acostumados a utilizar e o DNS que faz o trabalho de reconhecer cada domínio e devolver o endereço de IP para o navegador conseguir acessar o servidor desejado.

---

# Portas

Quando especificamos um domínio no navegador para acessar um site por exemplo, no HTTP por padrão ele implicitamente solicita o acesso através da **porta 80** o que na pratica seria:

http://www.alura.com.br:80

A porta de acesso sempre vem após o domínio, precedido de dois pontos.

Já no protocolo HTTPS a porta padrão utilizada é a 443

O FTP utiliza a 21

O SSH utiliza a 22

---

# Recursos

Conforme vamos navegando por um determinado site, podemos observar que a URL altera, muitas vezes acrescentando novos elementos, exemplo:

https://www.alura.com.br:443/curso-introducao-html-css

A parte destacada em amarelo, após a barra ao final do domínio, são chamados de **recursos** 

---

# URL - URI - URN

Muitas vezes, desenvolvedores usam a sigla **URI** (***U**niform* ***R**esource* ***I**dentifier*) quando falam de endereços na web. Alguns preferem **URL** (***U**niform* ***R**esource* ***L**ocator*), e alguns misturam as duas siglas à vontade. Há uma certa confusão no mercado a respeito e mesmo desenvolvedores experientes não sabem explicar a diferença. Então, qual é a diferença?

**Resposta 1 (fácil):** Uma **URL** é uma **URI**.

No contexto do desenvolvimento web, ambas as siglas são válidas para falar de endereços na web. As siglas são praticamente sinônimos e são utilizadas dessa forma.

**Resposta 2 (mais elaborada):** Uma **URL** é uma **URI**

Mas nem todas as **URI's** são **URL's**! Existem **URI's** que identificam um recurso sem definir o endereço, nem o protocolo. Em outras palavras, uma **URL** representa uma *identificação* de um recurso (**URI**) através do endereço, mas nem todas as identificações são **URL's**.

Humm ... ficou claro? Não? Vamos dar um exemplo! Existe um outro padrão que se chama **URN** (***U**niform* ***R**esource* ***N**ame*). Agora adivinha, os **URN's** também são **URI's**! Um **URN** segue também uma sintaxe bem definida, algo assim **`urn:cursos:alura:course:introducao-html-css`**. Repare que criamos uma outra identificação do curso **Introdução ao HTML e CSS** da Alura, mas essa identificação não é um endereço.

![https://s3.amazonaws.com/caelum-online-public/http/http-uri-urn-url.png](https://s3.amazonaws.com/caelum-online-public/http/http-uri-urn-url.png)

Novamente, a resposta 2 vai muito além do que você realmente precisa no dia a dia. *Normalmente **URL** e **URI** são usados como sinônimos*.