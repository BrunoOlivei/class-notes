def conta_ate(valor_maximo: int):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1


gen = conta_ate(5)
# print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))