# Pacotes

Assunto: Pacotes
Estudado: October 29, 2020 1:00 PM
Módulo: Módulos e Pacotes
Revisado: October 30, 2020 12:38 PM

## Diferença Módulo e Pacote:

**Módulo:** é apenas um arquivo Python que pode ter diversas funções para utilizarmos.

**Pacote:** É um diretório contendo uma coleção de módulos.


>[!Note]
> As versões antigas do Python 2.x, um pacote deveria conter dentro dele um arquivo chamado __init__.py. As versões a partir da 3 não exigem mais a utilização deste arquivo, porém ainda é utilizado para manter compatibilidade com os programas em versões anteriores.

## Criando um pacote no PyCharm:

![Clique com botão direito em cima do projeto, selecione 'New', e escolha Python Package.](Captura_de_tela_2020-10-29_130848.jpg)

Clique com botão direito em cima do projeto, selecione 'New', e escolha Python Package.

Dentro do pacote criamos arquivos python onde serão definidas funções:

![Pacotes%200e49950733e9427d80f2f27c85b5312d/SharedScreenshot1.jpg](SharedScreenshot1.jpg)

Em um outro arquivo python podemos então fazer referência dos arquivos criados dentro do pacote e também as suas funções:

```python
from Exemplo_Pacote import funcao1, funcao2

print(funcao1.minha_soma(5, 10))
print(funcao2.meu_nome())
```

Outra maneira de importar uma função é através:

```python
from Exemplo_Pacote.funcao1 import minha_soma

print(funcao1.minha_soma(5, 10))
```

Para importar um sub-pacote:

```python
from Exemplo_Pacote.Exemplo_SubPacote import funcao3, funcao4
```

