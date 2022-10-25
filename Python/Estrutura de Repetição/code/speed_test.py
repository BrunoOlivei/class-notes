# Teste de velocidade
import time

# Generator Expression
gen_inicio = time.time()

print(sum(num for num in range(100000000)))

gen_tempo = time.time() - gen_inicio

# List Comprehension

list_inicio = time.time()

print(sum([num for num in range(100000000)]))

list_tempo = time.time() - list_inicio

print(f"Tempo de execução do Generator Expression: {gen_tempo}")
print(f"Tempo de execução do List Comprehension: {list_tempo}")