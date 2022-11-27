# Por que dados são o novo petróleo

O petróleo é tão valioso pois existe uma gama enorme de produtos e serviços que dependem dele como matéria-prima, se não houvesse, ele não possuíria tanto valor.

Já o dado é tratado como matéria-prima para obtenção de informações e novos conhecimentos, por isso é constantemente comparado ao petróleo.

Alguns exemplos da tomada de decisão com dados:

Metallica utiliza dados do spotify para montar o setlist para o show de acordo com as musicas mais tocadas para a região.

Durante o próximo torneio da Copa do Mundo de futebol no Catar, os jogadores terão uma maneira mais baseada em evidências para argumentar pelo tempo em campo. Minutos após o apito final, os organizadores do torneio enviarão a cada jogador uma análise detalhada de seu desempenho. Os atacantes poderão mostrar com que frequência eles fizeram uma correram para receber a bola mas foram ignorados. Os defensores terão dados sobre o quanto eles enganaram e atormentaram a equipe adversária enquanto ela tinha posse.

Em 2022 o governo do Canada lançou um documento com as propostas e planos de ambição para um Canada Digital, baseado em dados. 

Nessa matéria da Forbes trás uma perspectiva sobre governos orientados a dados e o que podemos esperar para os proximos anos, baseado em um documento da ONU.


## Exemplos de aplicações nos esportes:

🏉 **Rugby:** Em 2019, a South African Rugby Union fez uma parceria com a _Microsoft_ para análise de dados com uma **plataforma de estratégia digital** — chamada _Stratus Reporting Engine_ — para ajudá-los a se preparar para o torneio. O objetivo, segundo Jurie Roux, CEO da South African Rugby era se posicionar como uma equipe vencedora, o que acabou realmente acontecendo quando a equipe ganhou sua 2° Copa Mundial de Rugby em novembro do mesmo ano.

🏀 **Basquete:** As equipes da NBA têm **explorado as imagens** capturadas por câmeras de última geração, instaladas ao redor de seus estádios e arenas, para capturar as ações de cada jogador, suas posições e a correspondente análise da movimentação dos oponentes. Essas imagens fornecem aos cientistas de dados a oportunidade de realizar uma análise aprofundada para a equipe técnica, com utilização de ferramentas de mineração de dados e inteligência artificial.

🏊 **Natação:** Na Finlândia, as equipes nacionais de natação tem usado uma abordagem de análise técnica baseada em **dados capturados por um acessório** chamado _SmartPaddles Trainesense_. É realizada uma análise biomecânica para dar aos atletas e treinadores informações sobre os pontos fortes e fracos de cada nadador. Esse acessório mede a força e a velocidade da mão, bem como a direção da força na água, provendo informações importantes sobre os desempenhos nos treinos.

**Mas e para empresas?** Cada vez mais empresas têm adotado o conceito de DATA DRIVEN.

Data Driven é muitas vezes associada a cultura de uma empresa, por isso ouvimos muitas vezes o termo Data Driven Culture. Que nada mais é do que uma "filosofia de atuação" que coloca os dados no cerne das decisões das empresas, tratando os dados como matéria prima primordial para novos conhecimentos, a partir dessa cultura temos diversas aplicações:
1. Data Driven Marketing
2. Data Driven UX
3. Data Driven Desing

---
# Fazes do dado

## Extração Tratamento e Carregamento

Extração dos dados de locais distintos, pensando em formas de governança, de forma estruturada e estabelecê-los conforme regras de negócio, respeitando padrões para que análistas e ciêntistas consigam trabalhar.

Exemplo: base de dados coletadas em vários países, para identificar um usuário usualmente usa-se o CPF em outros países o identificador pode conter outra formatação, como, por exemplo letras, dígitos, etc. 

Por isso a importância de conhecer sobre o negócio, visualizando as necessidades que surgirão a partir do dado bruto, e estruturar tentando atender as necessidades do ciclo de vida de um dado, que inicial na captação até o produto, passando por análise, treinamento de modelos de machine learning. Vale ressaltar a importância da escalabilidade, segurança e integridade, sem que comprometa o fluxo. 

## Análise

Obter insights através da utilização de álgebra, estatística, probabilidade e técnicas de visualização de dados e story telling para apresentação dos resultados das análises dos dados coletados e tratados anteriormente. Nessa etapa o ideal é que os dados já estejam coerentes com a necessidade.

Nessa etapa é importante ter em mente qual pergunta deseja ser respondida. Isso é importante e bebe da ciência tradicional, cujo todo e qualquer pesquisa parte de uma pergunta, por exemplo, se determinada proteína ou combinação de diversas é eficiente no tratamento de diabétes. Trazendo para o cenário empresárial, qual a probabilidade de um cliente cancelar os serviços? 

## Treinamento e Validação

Ainda com o problema em mente, aqui define-se quais algoritmos serão utilizados. Essa é a fase de experimentação, cujo ciêntistas de dados estão presentes. Com os dados tratados eestruturados da primeira etapa e categorizados após a análise, separam-se em 3 grupos (treino, teste e validação) conforme o Ramon explicou na tech meeting anterior. 

A validação vai definir se o modelo possui uma acurácia próxima da realidade, caso não, será necessário avaliar a utilização de outro modelo, ou a etapa de processamento dos dados alterando as variáveis ou até mesmo a de coleta caso seja percebido a necessidade de mais dados.

## Deploy e Monitoramento

Disponibilizar o modelo para que outros serviços possam acessar, seja dentro do ecossistema da empresa ou diretamente para os clientes.

Monitorar o andamento e quando é hora de capturar os dados e retreinar os dados.

Exemplo é na pandemia, um modelo treinado com dados anteriores a pandemia, não vão refletir a realidade. 
