# Criando um executável a partir de um programa Python | Alura Cursos Online

Assunto: Exe
Estudado: October 23, 2020 1:57 PM
Revisado: October 23, 2020 1:58 PM
URL: https://www.alura.com.br/artigos/criando-um-executavel-a-partir-de-um-programa-python

Aprenda a solucionar essa questão, congelando um arquivo Python em um simples executável,com o **cx_Freeze** e compartilhe suas aplicações com mais gente!"

![Criando%20um%20executa%CC%81vel%20a%20partir%20de%20um%20programa%20Pyt%201b70ea4400d94c9682a0415c6098a63a/code.jpg](code.jpg)

Recentemente, andei trabalhando em um simples projeto em **Python** para cálculo de IMC. Meu código simplesmente pega o input de altura e peso do usuário e imprime o IMC com a fórmula **Peso / Altura²**:

```

peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura * altura)

print('Seu IMC é {}'.format(imc))

```

O programa funciona bem, podemos até testar:

```

python imc.py
Digite seu peso: 90
Digite sua altura: 1.80
Seu IMC é 27.777777777777775
```

Certo! Gostei do resultado e resolvi mostrar para alguns amigos. O problema é que, como eles não são programadores, não tinham **Python** instalado na máquina deles.

E agora? Vou ter que pedir para eles instalarem o interpretador Python, ou uma IDE, apenas para rodar meu pequeno programa? Ou pior, será que eu mesmo vou ter que instalar no computador deles, já que eles não entendem muito disso?

Dando uma olhada no meu computador, percebi que tenho vários programas instalados que executam arquivos sem a necessidade de eu instalar um interpretador ou algo do tipo. Como eles fazem isso? E se a gente fizesse o mesmo?

O ideal seria se conseguíssemos transformar nosso arquivo

`imc.py` em um executável mais genérico (como é qualquer executável no Linux, ou os `.exe` no Windows), que pudesse rodar sem problemas. Felizmente, isso é até que bem simples!

### Congelando nosso programa Python com o `cx_Freeze`

A ideia de transformar um programa`.py` em um executável comum não começou com a gente, como você deve imaginar.

Assim, hoje em dia já existem diversas ferramentas e scripts que podem fazer todo esse processo de conversão para gente, como o **[PyInstaller](https://www.pyinstaller.org/)**, o [py2exe](http://www.py2exe.org/) e o **[cx_Freeze](https://anthony-tuininga.github.io/cx_Freeze/)**.

Usaremos o **cx_Freeze**, por ser multi-plataforma e de simples usabilidade. O primeiro passo, como sempre, é instalar esse pacote Python. Para isso, usamos o [pip](https://pypi.org/), no terminal:

```
pip install cx_Freeze

```

> Em sistemas baseados em UNIX, é possível que esse comando necessite de permissão sudo para funcionar
> 

Instalado o pacote, com um simples comando no terminal podemos já criar nosso executável. O comando base é simplesmente `cxfreeze`, mas, como queremos organizar um pouco melhor, usaremos a *flag* `-target-dir` para indicar a pasta onde queremos que fique nossos arquivos:

```
cxfreeze imc.py --target-dir calculadora-imc
```

Depois de um longo *output*, a pasta `calculadora-imc` é criada. Dentro dela, temos a seguinte organização:

![Criando%20um%20executa%CC%81vel%20a%20partir%20de%20um%20programa%20Pyt%201b70ea4400d94c9682a0415c6098a63a/imcls.png](imcls.png)

Os arquivos dentro da pasta `lib` e o `libpython3.6m.so.1.0` são arquivos de biblioteca que contém os dados necessários para que o executável funcione. Por sua vez, o arquivo `imc` (no Windows se chamaria `imc.exe`) é o executável.

Podemos até testá-lo:

![Criando%20um%20executa%CC%81vel%20a%20partir%20de%20um%20programa%20Pyt%201b70ea4400d94c9682a0415c6098a63a/imc.png](imc.png)

Funciona bem, e sem precisar da instalação do **Python**!

> É importante perceber que, como eu usei o _cxFreeze no Linux, esse executável só deve funcionar no Linux. Para criarmos um executável no Windows, o ideal seria rodar o _cxFreeze também no Windows.
> 

### Portabilizando nosso código para maior acesso

O Python, por diversas razões, é uma linguagem de programação incrível! Entretanto, uma de suas características que, por vezes, pode acabar decepcionando alguns usuários, é de que um programa Python só vai funcionar se o computador tiver o interpretador do Python instalado.

Isso acaba se tornando um pouco chato em situações que queremos compartilhar nosso programa com não-programadores, que dificilmente terão o Python instalado (especialmente se utilizarem o Windows, já que o Python vem por padrão em muitas distribuições baseadas em Unix), ou até mesmo com pessoas que têm instalada apenas uma versão diferente da que trabalhamos em nosso código.

Por conta disso, vários scripts foram criados para converter um arquivo `.py` em um simples executável que poderia funcionar sem a instalação do Python. Hoje, abordamos o **cx_Freeze**, que é multiplataforma e bem simples de usar!

#exe #executável