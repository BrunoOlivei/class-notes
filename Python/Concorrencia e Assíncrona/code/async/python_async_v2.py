import datetime
import math
import asyncio


def main():
    print("Realizando o processamento matemático de forma assíncrona")

    event_loop = asyncio.get_event_loop()

    inicio = datetime.datetime.now()

    # event_loop.run_until_complete(computar(inicio=1, fim=50_000_000))

    tarefa1 = event_loop.create_task(computar(inicio=1, fim=10_000_000))
    tarefa2 = event_loop.create_task(computar(inicio=10_000_001, fim=20_000_000))
    tarefa3 = event_loop.create_task(computar(inicio=20_000_001, fim=30_000_000))
    tarefa4 = event_loop.create_task(computar(inicio=30_000_001, fim=40_000_000))
    tarefa5 = event_loop.create_task(computar(inicio=40_000_001, fim=50_000_000))

    tarefas = asyncio.gather(tarefa1, tarefa2, tarefa3, tarefa4, tarefa5)
    result = event_loop.run_until_complete(tarefas)

    print(result)


    tempo = datetime.datetime.now() - inicio

    print(f"Tempo de execução: {tempo.total_seconds():.2f} segundos")


async def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        return math.sqrt((pos - fator) * (pos - fator))


if __name__ == "__main__":
    main()


"""
Tempo de execução: 21.78 segundos
"""
