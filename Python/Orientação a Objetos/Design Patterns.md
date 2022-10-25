# Decorator

Imagine que estamos implementando uma sequência de filtros. Esses filtros precisam eliminar diversas faturas de uma lista, de acordo com algumas regras de negócio: faturas menores que 2000 devem ser eliminadas, faturas maiores do que 8000 devem ser eliminadas, faturas entre 3000 e 4500 que foram emitidas no estado de São Paulo devem ser eliminadas, e assim por diante.

Uma implementação procedural produziria uma sequência de `ifs` enorme para verificar todas essas condições. Dentre os padrões de projeto aqui aprendidos, qual se encaixa melhor para esse problema?

O Decorator se encaixaria bem nesse problema. Poderíamos fazer com que cada filtro seja um "Decorator", e vamos decorando a lista com todos os filtros existentes. Cada filtro teria sua própria classe, simples e fácil de ser compreendida e mantida.

---

# Observer

Imagina que você precise avisar 3 sistemas externos (auditoria, financeiro, e agências), assim que uma conta bancária receber um depósito.

Em uma implementação procedural, todas essas atividades seriam invocadas logo após a operação de depósito, fazendo com que essa classe perca coesão, e fique complicada de ser entendida e mantida.

Dentre os padrões de projeto aqui aprendidos, qual se encaixa melhor para esse problema?

O Observer se encaixaria muito bem. Ele permite que você notifique e execute ações após algum acontecimento no seu sistema. E faz isso de tal forma que o acoplamento entre classes continue baixo, e flexível para adicionar novas ações quando necessário.

---

# Template Method

Imagine que temos uma série de algoritmos matemáticos a serem implementados. Todos eles são bem parecidos, possuem a mesma estrutura. As variações são mínimas, por exemplo, um deles deve iterar até o fim da lista, enquanto o outro deve iterar até a metade dela.

Uma implementação procedural possuiria uma alta repetição de código, já que os algoritmos são muito parecidos.

Dentre os padrões de projeto aqui aprendidos, qual se encaixa melhor para esse problema?

O Template Method cairia como uma luva, já que ele possibilita que o desenvolvedor escreva a "estrutura" do algoritmo apenas uma vez, e a reutilize nas implementações específicas de cada um dos algoritmos.

Isso faz com o que o código fique mais simples, possibilita que mudanças na estrutura desses algoritmos sejam facilmente modificadas, e que novos algoritmos sejam criados de forma simples.

---

# State

Um Contrato pode sofrer tipos de alterações, descontos, ajustes enquanto está EM ANDAMENTO. O mesmo pode acontecer quando ele está FALTANDO ASSINATURA DO CLIENTE. Mas, após ASSINADO, o contrato não pode mais sofrer alterações.

Um código procedural muito provavelmente conteria um conjunto enorme de `ifs`, um para cada possível estado do Contrato e ação a ser executada, tornando o código desnecessariamente complexo e difícil de ser mantido.

Dentre os padrões de projeto aqui aprendidos, qual se encaixa melhor para esse problema?

O State facilitaria o trabalho do desenvolvedor, já que ele possibilitaria que as ações de cada estado fiquem centralizadas em classes específicas, evitando a possível bagunça de um código procedural cheio de `ifs`.

Além disso, criar novos estados para esse contrato também seria fácil.

---
#designpattern #decorator #observer #templatemethod #state