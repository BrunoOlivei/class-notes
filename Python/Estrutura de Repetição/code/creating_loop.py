def meu_iteravel(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_iteravel("Hello World")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
meu_iteravel(numeros)

"""
Criando um loop customizado
"""

class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor += 1
            return numero
        else:
            raise StopIteration


contador = Contador(1, 10)
for numero in contador:
    print(numero)
