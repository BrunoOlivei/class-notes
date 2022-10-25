import datetime
import asyncio


async def gerador_dados(quantidade: int, dados: asyncio.Queue):
    print(f"Aquarde a geração de {quantidade} dados")
    for idx in range(1, quantidade + 1):
        item = idx * idx
        await dados.put((item, datetime.datetime.now()))
        await asyncio.sleep(0.001)
    print(f"Geração de {quantidade} dados concluída")


async def consumidor_dados(quantidade: int, dados: asyncio.Queue):
    print(f"Aguarde o processamento de {quantidade} dados")
    processados = 0
    while processados < quantidade:
        await dados.get()
        processados += 1
        await asyncio.sleep(0.001)
    print(f"Processamento de {quantidade} dados concluído")

if __name__ == '__main__':
    total = 5000
    dados = asyncio.Queue()
    eventloop = asyncio.get_event_loop()

    print(f"Computado {total * 2:.2f} dados")

    eventloop.run_until_complete(gerador_dados(total, dados))
    eventloop.run_until_complete(gerador_dados(total, dados))
    eventloop.run_until_complete(consumidor_dados(total * 2, dados))

    eventloop.close()
