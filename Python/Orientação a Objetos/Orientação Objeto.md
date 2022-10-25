# Introdução:

O python utiliza o método `class` para definir um objeto na linguagem. 

Dentro dele é usual definir uma função nomeada com uma função *dunder* no caso `__init__` para atribuir as características do objeto ou seja os **atributos:**

```python
class Conta:
    
    def __init__(self):
				print("Criando Objeto...")

```

Nos códigos escritos sob o paradigma da orientação a objeto, é muito comum encontrar uma variável recebendo como valor o nome de uma determinada class (objeto). Quando isso ocorre os programadores dizem que a variável é a **referencia** do objeto.

```python
conta = Conta()
```

Isso por que o objeto Conta tem um endereço na memória do computador, mas cada vez que a classe é chamada ele cria um novo endereço. Então para que não percamos a referência desse endereço de memória toda vez que precisemos utilizar aquele objeto ele é atribuído a uma variável que no caso se torna uma **referencia** .

---

## (Self)

O que o self representa dentro da função `__init__`?

Se observarmos o próprio __init__ é uma função que recebe também um atributo dentro dos seus parênteses. 

No caso aqui vamos pedir para imprimir o self no console e verificar o que se trata:

```python
class Conta:
    
    def __init__(self):
				print("Criando Objeto... {}".format(self))

>>> conta = Conta()
Construindo Objeto... <conta.Conta object at 0x00000173C013FF70>
>>> conta
<conta.Conta object at 0x00000173C013FF70>
```

`self` é a referência que sabe encontrar o objeto construído em memória.

---

# Criando um Construtor:

Definida a classe e a função que inicializa automaticamente a criação da classe, chegada a hora de criar os atributos que serão as características deste objeto e receberão os valores. Podemos fazer uma analogia a um carro, que possui suas características como potência do motor, tipo de combustível utilizado, autonomia, torque etc. 

```python
class Conta:

		def __init__(self, numero, titular, saldo, limite):
          print("Criando Objeto... {}".format(self))
					self.numero = numero
					self.titular = titular
					self.saldo = saldo
					self.limite = limite
```

No `self.numero` o ponto (.) é um comando de "ida" ao objeto e `numero`, `titular`, `saldo` e `limite` são os atributos.

O que queremos dizer aqui é que a função `__init__()` acesse, crie ou altere os valores dos atributos. 

Ao atribuirmos para cada objeto `self.` um "valor" precisamos atribuir como parâmetro na função `__init()__` para que o objeto seja acessado e alterado.

Agora é só testar:

```python
>>> from conta import Conta

>>> conta = Conta(123, "Bruno", 100.0, 1000.0)
Construindo objeto ... <conta.Conta object at 0x11077bcc0>

>>> conta2 = Conta(321, "Marco", 55.0, 1000.0)
Construindo objeto ... <conta.Conta object at 0x1109e1da0>
```

>[!note]
>No início das definições de classe, é um consenso dentro da comunidade python, que os atributos criados sejam o mínimo necessário para começar a trabalhar. Um exemplo prático é a criação de uma classe Cliente. Nós tendemos a ficar tentados a iniciar criando o máximo de informação possível, do nome até o nível escolar, passando por estado civil e etnia. Porém dentro do seu contexto quais informações realmente são importantes e quais podemos deixar para um momento futuro?

# Acessando atributos

Com os objetos e seus atributos criados, será que é possível acessá-los tanto para consultas como para tarefas mais complexas como usar em uma outra função que execute determinado operação?

Utilizando a linhagem UML que serve para descrever de forma visual através de gráficos e desenhos um sistema por exemplo, temos o seguinte:

![4%20Orientac%CC%A7a%CC%83o%20Objeto%202f029f77a9684c3db113bf6fd135d15f/2.7_2_diagramasdeclassecomatributos.png](2.7_2_diagramasdeclassecomatributos.png)

## Estrutura:

1. **conta.py**: é o módulo, em algumas linguagens pode ser reconhecido como `package` ou `namespace` dentro dele poderíamos ter mais de uma sintaxe. 
2. **Conta:** É a classe criada. ela está contida dentro do módulo conta.py
    
    <aside>
    📌 Por isso quando vamos executar no console python, precisamos fazer o import deste módulo e da classe conta, através do `from conta import Conta`
    
    </aside>
    
3. **numero, titular, saldo e limite:** são os atributos da classe Conta

## E cadê o __init()__?

Ele não é exibido no diagrama de classes, porque se trata de uma função implícita, que é chamada automaticamente. 

Quando chamamos a classe Conta(), por baixo dos panos o Python passará os valores para a função `__init()__`. Quando executamos a linha com a referência **conta,** em memória, o python irá gerar o objeto em que são guardados os valores:

  

![4%20Orientac%CC%A7a%CC%83o%20Objeto%202f029f77a9684c3db113bf6fd135d15f/2.7_3_classeContaadicionada.png](2.7_3_classeContaadicionada.png)

A partir daqui python criou um objeto conta com os atributos como numero, titular, saldo e limite definidos, a partir do momento que passamos estes valores dentro dos parênteses, em uma referencia com nome conta.

---

# Acessando valores

Com objeto criado, podemos acessar os seus valores utilizando os atributos:

A primeira conta criada tem como referencia a palavra 'conta':

```python
>>> conta = Conta(123, "Bruno", 55.0, 1000.0)
>>> conta2 = Conta(321, "Marco", 100.0, 1000.0)
```

Para acessar utilizamos a referencia seguida de ponto e o nome do atributo:

```python
>>> conta.titular
'Bruno'
>>> conta.saldo
55.0
>>> conta2.titular
'Marco'
>>> conta2.numero
321
```

---

# Métodos

Métodos basicamente são as funcionalidades que um objeto tem ou pode fazer. Podemos pensar em um carro, que só pode andar para frente ou para trás ou ficar parado. 

Para definir uma funcionalidade (método):

```python
class Conta:

		def __init__(self, numero, titular, saldo, limite):
          print("Criando Objeto... {}".format(self))
					self.numero = numero
					self.titular = titular
					self.saldo = saldo
					self.limite = limite
		
		def extrato(self):
					print('Saldo {} do títuluar {}'.format(self.saldo, self.titular))

```

Dessa vez definimos um nome a função que será o método 'extrato', esse que irá imprimir na tela o valor de saldo do cliente. 

`def extrato(self):`

Como parâmetro o self novamente é informado, isso se deve pois ele precisa acessar a referência da classe em que está inserida e todos os atributos que a classe possui.

Como retorno vamos imprimir uma string que receberá os saldo e o nome do titular, através da formatação do string.

`print('Saldo {} do títuluar {}'.format(self.saldo, self.titular))`

Mais uma vez o self aparece pelo mesmo motivo de buscar a própria referência. 

## Executando:

Executando o método extrato:

Novamente dentro do console, importamos a classe e criamos as contas de exemplo:

```python
>>> from conta import Conta

>>> conta = Conta(123, "Bruno", 55.0, 1000.0)
Construindo objeto... <conta.Conta object at 0x000001AE182B7280>

```

Agora para chamarmos o método extrato:

```python
>>> extrato()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'extrato' is not defined
```

Recebemos um erro dizendo que extrato não foi definido. Mas nós escrevemos corretamente, a criação da conta de exemplo ocorreu tudo bem o que falta?

<aside>
📌 FALTA A REFERÊNCIA

</aside>

Sim imagine se tivéssemos 10, 50, 100, Um milhão de contas criadas, ao executar o comando `extrato()` estamos solicitando o extrato de quem?

É ai que entra novamente a referência conforme vimos anteriormente quando queríamos acessar o nome do titular por exemplo. Então a sintaxe para execução do método "extrato" fica da seguinte maneira:

```python
>>> conta.extrato()
Saldo 55.0 do titular Nico.
```

Agora sim executada de forma correta. 

---

## Mais métodos:

Agora podemos criar alguns métodos que podem ser úteis para uma conta bancária, como por exemplo depósito e saque de valores. 

```python
class Conta:

		def __init__(self, numero, titular, saldo, limite):
          print("Criando Objeto... {}".format(self))
					self.numero = numero
					self.titular = titular
					self.saldo = saldo
					self.limite = limite
		
		def extrato(self):
					print('Saldo {} do títuluar {}'.format(self.saldo, self.titular))

		def deposita(self, valor):
					self.saldo += valor

		def saca(self, valor):
					self.saldo -= valor
```

No caso destes 2 novos métodos, precisamos receber um valor como argumento para que possamos realizar as operações pertinentes para alterar o saldo. 

No caso de depósitos o valor recebido como argumento será adicionado ao saldo, enquanto o método saca o valor irá subtrair do saldo. Para isso é necessário parametrizar em cada método, além do self, um valor que será utilizado para as operações. 

```python
>>> from conta import Conta

>>> conta = Conta(123, "Nico", 55.5, 1000)
Construindo objeto... <conta.Conta object at 0x000002393068FF70>

>>> conta.extrato()
Saldo 55.5 do titular Nico.

>>> conta.deposita(15.0)
>>> conta.extrato()
Saldo 70.5 do titular Nico.

>>> conta.saca(10)
>>> conta.extrato()
Saldo 60.5 do titular Nico.

```

---

# None e Coletor de Lixo

Imagine a seguinte situação:

Suponhamos que dentro do nosso programa onde temos uma conta criada com a referência *'conta1'* com todos os seus atributos como número da conta, tiular da conta, valor do saldo e o valor do limite.

Agora imagine que por algum motivo hipotético nós executamos a classe para uma referencia de mesmo nome *conta1*, com os mesmos valores para os atributos, algo como:

```python
>>> conta1 = Conta(123, "Nico", 55.0, 1000.0)
>>> conta1 = Conta(123, "Nico", 55.0, 1000.0)
```

Nós literalmente criamos 2 objetos com a mesma referencia. É isso mesmo que acontece, foram criados 2 objetos utilizando a mesma referencia. Só que esta referência não irá apontar para os 2 objetos ao mesmo tempo, um deles ficará perdido na memória ocupando espaço, sem uma referencia para que possamos acessá-la. 

Ou seja:

O que temos é uma referencia com nome conta atribuída a um objeto na memória enquanto outro não possui nenhuma referencia. 

Porém a linguagem python e muitas outras possui uma funcionalidade que automaticamente procura os objetos na memória que não possuem referencia, isso é chamado de *garbage collector* (coletor de lixo)

![4%20Orientac%CC%A7a%CC%83o%20Objeto%202f029f77a9684c3db113bf6fd135d15f/coletor_lixo.png](coletor_lixo.png)

Outra possibilidade seria querermos *"desatribuir"* uma referencia a um objeto na memória, podemos fazer isso utilizando o `None`: 

```python
>>> conta = None
```

Simples assim.

---

# Encapsulamento

Encapsulamento é uma das principais características da programação orientada a objetos.

Usando como exemplo o nosso objeto Conta, que possui atributos como saldo, número da conta, nome do titular e limite, e métodos que são as funções sacar, depositar e extrato, todos estes são facilmente acessáveis e alteráveis. Essa facilidade pode ser um risco para a integridade do sistema em questão, onde qualquer pessoa com acesso a esses atributos e métodos poderá alterar alguma coisa e comprometer o resultado do sistema, sem contar possíveis ataques maliciosos.

## Atributos Privados

Vamos relembrar um pouco como podemos acessar algumas informações do nosso objeto conta. Lembrando que criamos alguns métodos, uma atenção especial ao 'extrato()' que retorna o nosso saldo. 

Porém também podemos acessar essa mesma informação através de `conta.saldo`, mas não nós podemos além disso alterar o valor manualmente. Pensando numa implementação como está em uma situação real do cotidiano seria catastrófico essa liberdade de acesso.

```python
>>> from conta import Conta
>>> conta = Conta(123, 'Nico', 55.0, 1000.0)
Construindo objeto... <conta.Conta object at 0x000001A4F9D9FDC0>
>>> conta.saldo
55.0
>>> conta.saldo = 55000
>>> conta.extrato()
Saldo 55000 do titular Nico. 
```

Para isso existem os atributos privados e para criarmos isso basta adicionarmos dois underlines (__) no começo do nome do atributo, desta forma:

```python
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
```

Também é necessário colocarmos nos métodos:

```python
def extrato(self):
        print('Saldo {} do titular {}.'.format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor
```

Reiniciando o console, vamos importar novamente o módulo e criar uma conta:

![4%20Orientac%CC%A7a%CC%83o%20Objeto%202f029f77a9684c3db113bf6fd135d15f/1_atributo_privado.jpg](1_atributo_privado.jpg)

Observe que a partir do momento que inserimos o ponto ( . ) o PyCharm já abre algumas opções, podemos ver que ainda aparece para nós os atributos saldo, limite etc. porém com uma notação diferente, repare que há um underline (_) antes da classe Conta e dois underlines **(__) antes do atributo.

Esse tipo de anotação, no caso das classes, representa exatamente o que queremos, que aquele atributo é privado.

<aside>
⚠️ Mesmo tendo formatado para que o atributo seja privado, ainda conseguimos acessar e até alterar o valor. O python não proíbe que você acesse e altere o conteúdo, o que ele faz é criar essa notação com underline antes de nome da classe e dois antes do nome do atributo para SINALIZAR ao desenvolvedor que este atributo é privado e que o acesso e alteração é por conta e risco do programador.

</aside>

No universo OO do python esta forma de privatizar um atributo utilizando os dois underscores (__) antes do nome é chamada de desfiguração de nomes (name mangling). 

Ficou claro que não é uma forma de assegurar que determinado atributo não seja alterado em caso  malicioso, a unica função dele aqui é proteção como dito anteriormente é uma forma de sinalizar o programador que aquele atributo NÃO DEVERIA ser mexido.

---

## Organização e métodos privados

Utilizando novamente o exemplo da classe Conta com duas contas distintas armazenadas e com referência diferentes, vamos tentar fazer uma transferência entre 2 objetos Conta:

```python
>>> from conta import Conta
>>> conta1 = Conta(123, 'Queiroz', 89000.0, 1000000)
Construindo objeto... <conta.Conta object at 0x00000190951DFA00>
>>> conta2 = Conta(321, 'Michele', 0.0, 100000)
Construindo objeto... <conta.Conta object at 0x0000019095202670>
```

Até o momento nós já temos alguns métodos a disposição como o saca e deposita, nós poderíamos realizar da seguinte forma:

```python
>>> valor = 89000
>>> conta1.saca(valor)
>>> conta2.deposita(valor)
```

Agora vamos verificar utilizando o método `extrato()` que criamos anteriormente:

```python
>>> conta1.extrato()
Saldo 0.0 do titular Queiroz.
>>> conta2.extrato()
conta2.extrato()
Saldo 89000.0 do titular Michele.
```

Basicamente isso é uma transferência e nós implementamos fora da classe, isso quebra o conceito de **Encapsulamento,** sendo o nosso objetivo um código organizado, precisamos implementar essa método dentro da classe.

<aside>
📌 Sobre as nomenclaturas de classes:
Temos a liberdade de utilizarmos as palavras nas suas diversas variáveis conjugações por exemplo no caso de verbos. Porém é consenso no mundo Python que uma vez escolhido a forma como o primeiro nome será dado, seguir utilizando a mesma conjugação. Exemplo: sacar, depositar, transferir.

</aside>

Para criarmos o método transfere, vamos cria-lo logo abaixo do método saca, utilizando mais uma vez a palavra reservada `def` para definir o método:

```python
def transfere(self):
```

O que queremos com transfere? Queremos que ele transfira um **valor**, para isso precisamos parametrizar que este método recebe um valor:

```python
def transfere(self, valor)

```

Reaproveitando o código passado, onde criamos fizemos a movimentação do Queiroz para Michele no valor de 89.000,00 utilizando o método saca e deposita, vamos implementar dentro do transfere estes mesmos métodos.

```python
def transfere(self, valor)
    origem.saca(valor)
    destino.deposita(valor)
```

Dentro do nosso método não existe origem nem mesmo destino, para isso precisamos então parametrizar que o método também recebe esta informação, para então executar os outros métodos (saca e deposita). Uma transferência entre contas do mesmo banco, geralmente nos basta o número da conta e a agencia para realizarmos transferências. No nosso caso nós já temos as referencias de cada conta criada, portanto nós só precisamos informar a referencia para conta de origem e a referencia para a conta de destino que o python se encarrega do resto:

```python
def transfere(self, valor, origem, destino)
    origem.saca(valor)
    destino.saca(valor)
```

### Testando:

```python
>>> from conta import Conta
>>> conta1 = Conta(123, 'Queiroz', 89000.0, 100000.0)
Construindo objeto... <conta.Conta object at 0x0000028343462A60>
>>> conta2 = Conta(321, 'Michele', 0.0, 100000.0)
Construindo objeto... <conta.Conta object at 0x0000028343462490>

>>> valor = 89000
>>> conta1.transfere(89000, conta1, conta2)

>>> conta1.extrato()
Saldo 0.0 do titular Queiroz.
>>> conta2.extrato()
Saldo 89000.0 do titular Michele.
```

Repare que na linha onde chamamos o método transfere nós escrevemos 2 vezes 'conta1', isso é mal sinal nosso código não está totalmente otimizado e escrito seguindo as melhores práticas. Funciona mas mesmo assim não é o ideal.

Se ao chamar o método para a conta em questão eu já estou referenciando ela através do `self`, não há necessidade de pedir como parâmetro novamente a conta de origem certo? 

Poderíamos então escrever o método transfere da seguinte forma:

```python
def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
```

Vamos ver se funciona:

```python
>>> from conta import Conta
>>> conta1 = Conta(123, 'Queiroz', 89000.0, 100000.0)
Construindo objeto... <conta.Conta object at 0x0000022C0F0D5BB0>
>>> conta2 = Conta(321, 'Michele', 0.0, 100000.0)
Construindo objeto... <conta.Conta object at 0x0000022C0F1A1B80>

>>> valor = 89000
>>> conta1.transfere(valor, conta2)

>>> conta1.extrato()
Saldo 0.0 do titular Queiroz.
>>> conta2.extrato()
Saldo 89000.0 do titular Michele.
```

Funciona perfeitamente, desta forma é até melhor pois ao pedir a conta de origem e a conta de destino pode causar confusão para o usuário.

---

# Propriedades

Nós já definimos um método chamado extrato para mostrar o saldo da conta do Queiroz e da Michele. Agora imagine que somos a policia federal e estamos exigindo que o banco em questão nos mostre quem é o titular de cada conta, além disso mostre também o limite que cada uma dessas contas possui.

Naturalmente poderíamos realizar chamando o atributo diretamente, mas lembrando que nós privatizamos ele, e que na teoria não devemos mexer mais diretamente nele. Para isso ele agora possuem uma nomenclatura diferente justamente para sinalizar isso. Então como podemos fazer? Podemos criar um método novo chamado **@properitiy**. Voltando a nossa classe conta: 

```python
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print('Saldo {} do titular {}.'.format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
```

Já temos os métodos para realizar operações no objeto Conta e também para imprimir o valor do saldo.

Agora queremos o titular, para demonstrar de quem é determinado valor, para isso criaremos mais um método utilizando mais uma vez o `def`:

Só que dessa vez ele terá algo a mais, antes de definirmos o método adicionamos **@properitiy**

```python
@property
def titular(self):
    return self.__titular
```

Agora vamos fazer um teste:

```python
>>> from conta import Conta
>>> conta1 = Conta(123, 'Queiroz', 89000.0, 100000)
Construindo objeto... <__main__.Conta object at 0x0000022931F26B80>

>>> conta1.titular
'Queiroz'
```

E se precisássemos alterar alguma dado de algum objeto como por exemplo o limite, pensando em nossa classe e no que ela propõe seria interessante que o limite pudesse ser alterado quando necessário. 

Porém lembrando que todos os atributos estão configurados para serem privados, ou seja, não é ideal que acessemos diretamente o atributo limite e façamos a alteração dele manualmente, para isso vamos utilizar um **setter,** mas antes também precisamos *settar* o limite como um *properity*: 

```python
@property
def limite(self):
    return self.__limite

@limite.setter
def limite(self, limite):
    self.__limite = limite
```

Agora o teste:

```python
>>> conta1 = Conta(123, 'Queiroz', 89000.0, 100000)
>>> Construindo objeto... <__main__.Conta object at 0x000001D160BFFE50>

>>> conta1.limite
100000

>>> conta1.limite = 89000
>>> conta1.limite
89000
```

<aside>
📌 Repare que agora podemos utilizar a sintaxe `objeto.atributo = valor` para atribuir um novo valor a ele.

</aside>

---

# Métodos Privados

Da mesma forma que temos os atributos privados, também temos os métodos privados. Estes podem ser aplicados para impedir que algum método que sirva somente para gerar um valor que será usado por outro método não seja facilmente utilizado e alterado, vamos usar mais uma vez a nossa classe conta.

```python
	class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print('Saldo {} do titular {}.'.format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite
```

Até o momento este é o nosso código. Relembrando o método saca que subtrai um valor informado do saldo da conta.

Pensando em uma implementação no mundo real o correto seria a nossa classe verificar se a conta possui saldo suficiente para realizar o saque, lembrando que o valor disponível será o saldo mais o limite. 

Naturalmente podemos utilizar um bloco de código if para chegar esse valor:

```python
def saca(self, valor):
    if valor <= (self.__saldo + self.__limite):
        self.__saldo -= valor
    else:
        print(f'O valor {valor} ultrapassou o limite')

```

Muito simples, mas seria interessante deixar o código mais expressivo e nítido para entendermos o que cada método realiza e o que esperar de resultado de cada um deles. 

## Refatorando:

Vamos criar um método que fará a verificação do saldo + limite:

```python
def pode_sacar(self, valor_a_sacar):
    valor_disponivel = self.__saldo + self.__limite
    return valor_a_sacar <= valor_disponivel
```

Neste método receberemos o valor solicitado, criamos uma variável que recebe a soma de saldo e limite e checamos se o valor solicitado é menor ou igual ao valor disponível.

Feito isso, agora o método saca receberá o método pode_sacar dentro dele:

```python
def saca(self, valor):
    if self.pode_sacar(valor):
        self.__saldo -= valor
    else:
        print(f'O valor {valor} ultrapassou o limite')
```

Agora o método saca vai receber um valor irá inicializar outro método, o pode_sacar que verifica se o valor solicitado é menor ou igual ao saldo disponível mais o limite e retornará um valor True em caso positivo e False caso o valor seja maior, isso retorna para o método saca onde através de outra estrutura condicional IF irá fazer o saque caso o valor retornado seja True ou imprimir uma mensagem informando o usuário que o valor ultrapassou o limite em caso de False.

```python
>>> conta1 = Conta(123, 'Queiroz', 89.0, 1000.0)
Construindo objeto... <__main__.Conta object at 0x0000010FC07CF9D0>

>>> conta1.saca(1200)
O valor 1200 ultrapassou o limite.

>>> conta1.pode_saca(1200)
False

>>> conta1.pode_saca(89)
True

>>> conta1.extrato()
Saldo 89.0 do titular Queiroz.
```

Observe que o método pode_saca que criamos para verificar se o valor de saque é menor que o saldo disponível mais o limite é totalmente acessível. Porém este método é de uso interno e não há necessidade de estar disponível e pode até comprometer o programa caso haja alteração. 

Por isso vamos torná-lo privado, assim como os atributos, basta adicionar dois underscores(__) antes do nome do método e fazer o mesmo onde o método estiver sendo chamado.

```python
def __pode_sacar(self, valor_a_sacar):
    valor_disponivel = self.__saldo + self.__limite
    return valor_a_sacar <= valor_disponivel

def saca(self, valor):
    if self.__pode_sacar(valor):
        self.__saldo -= valor
    else:
        print(f'O valor {valor} ultrapassou o limite')
```

---

# Métodos Estáticos (Static Methods)

São métodos característicos da classe, ou seja, não necessariamente precisam de um objeto para existir, eles já existem por si só a partir da classe.

Por exemplo uma clínica que possua apenas um médico atendendo, então no sistema todos os pacientes serão deste médico, ou o código do banco no BACEN, em um sistema de um banco específico todos os seus clientes possuem o mesmo código de banco. 

Usando novamente o exemplo do programa de banco nosso, vamos criar um método e utilizar o `@staticmethod`

```python
def codigo_banco():
    return '001'
```

Vamos testar:

```python
>>> conta1 = Conta(123, 'Queiroz', 89.0, 1000.0)
Construindo objeto... <__main__.Conta object at 0x0000021C9178F640>

>>> conta1.codigo_banco()
'001'
```

É possível também acessar os código dos bancos sem a necessidade de chamar um objeto, basta chamar o nome da classe seguida de ponto e o método estático:

```python
>>> Conta.codigo_banco()
'001'
```

---

# Atributo de Classe

O atributo de classe pode ser utilizado por exemplo:

```python
>>> class Circulo:

        PI = 3.14
```

Dessa maneira podemos chamar o método:

```python
>>> Circulo.PI
3.14

```