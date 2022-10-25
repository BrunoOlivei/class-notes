# Instalando e Utilizando Módulos Externos

Assunto: Módulos Externos (pip)
Estudado: October 29, 2020 11:34 AM
Materials: https://docs.python.org/pt-br/3.7/installing/index.html, https://pypi.org/
Módulo: Módulos e Pacotes
Revisado: October 29, 2020 12:12 PM

## Instalando

Através do gerenciador de pacotes Python que é incluído por padrão com os instaladores binários do python chamado pip.

O comando abaixo é inserido no terminal:

```python
python -m pip install nome_pacote
```

A baixo utilizamos o terminal do PyCharm, mas o principio é o mesmo independente se for utilizar o PowerShell ou qualquer outro terminal. 

![Instalando%20e%20Utilizando%20Mo%CC%81dulos%20Externos%20828d63fd19284c53877088a59d60d3d2/SharedScreenshot.jpg](SharedScreenshot.jpg)

É importante atentar para a instalação de pacotes dentro de ambientes virtuais, dessa forma somente o seu projeto terá acesso a determinado pacote e suas versões. Caso haja alguma atualização no pacote ou até mesmo na linguagem o seu programa não terá atualizado automaticamente evitando o risco de crash. 


>[!Note] 
>O site [pypi.org](http://pypi.org) é o local onde se encontram todos os pacotes e módulos já publicados, você pode conhecer mais sobre cada pacote pesquisando, visualizar uma lista dos mais populares e os mais novos lançamentos.
