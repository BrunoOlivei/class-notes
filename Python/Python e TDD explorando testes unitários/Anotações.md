# Metodologias

## **_Given-When-Then_**

- **_Given (dado - contexto)_** é o contexto que inícia o teste, por exemplo, se tenho dinheiro na conta para realizar uma compra, tenho uma data de nascimento para calcular a idade, tenho os dados de formulário para cadastrar algo em uma aplicação.

- **_When (quando - ação)_** é a ação que deve ser tomada a partir dos dados de contexto, por exemplo, realizar a compra caso haja saldo sulficiente, cálcular a idade com base na data de nascimento, persistir os dados no banco de dados a partir de um formulário preenchido.

- **_Then (Asserção)_** é o resultado que se espera da ação, por exemplo, saldo é igual ou maior que o valor do produto que se deseja comprar? A idade é igual a esperada? Os dados do formulário estão nos formatos corretos?

## **_Arrange-Act-Assert (AAA)_**

-   **_Arrange_**: A tradução não literal seria algo como **organizar**. A organização, nesse caso, seria focada nos passos preliminares necessários para montar o contexto inicial do teste;

- **_Act_**: A tradução não literal seria algo como **agir**. Nesse caso seria a ação que parte dos passos organizados na primeira etapa e leva ao que vamos averiguar no final;

- **_Assert_**: A tradução não literal seria algo como **averiguar**. Nesse caso, averiguarmos que o desfecho trazido pela ação é realmente aquele que esperamos.

# Cenários de testes

[Montando cenários de testes com o Pytest | Alura](https://www.alura.com.br/artigos/montando-cenarios-de-testes-com-o-pytest)

# Cobertura de testes

Com o pacote pytest-cov podemos checar qual a porcentagem de cobertura dos testes sobre o código. Após instalar o pacote através do `pip install pytest-cov`, podemos rodar os comandos no terminal:

`pytest --cov`  que trará uma tabela no terminal com os nomes dos arquivos, statements, quantos não foram cobertos pelo teste e a porcentagem de cobertura.

Porém esse comando análisa todos os arquivos `.py` do projeto.

![[Pasted image 20230424154034.png]]

`pytest --cov=codigo tests/` analisara apenas os arquivos de um diretório específico, que no caso é o diretório código.

![[Pasted image 20230424154304.png]]

## Como encontrar o que está faltando na cobertura dos testes

O comando no terminal `pytest --cov=codigo tests/ --cov-report term-missing` trará uma coluna extra que indica as linhas do arquivo que não estão sendo contemplada.

![[Pasted image 20230424154623.png]]

Uma outra forma de visualizar melhor as partes do código que não estão sendo cobertas pelos testes é utilizando o comando `pytest --cov=codigo tests/ --cov-report html` que irá criar uma pasta contendo arquivos HTML CSS e JS com as informações e inclusive uma cópia em HTML do código em python com destaque para as partes que não estão sendo cobertas pelos testes.

## Gerando relatórios

- Em xml: `pytest --junitxml report.xml` ou `pytest --cov-report xml`

