import threading
import time
import random
from typing import List

lock = threading.RLock()

class Conta:
    def __init__(self, saldo=0) -> None:
        self.saldo = saldo


def main():
    contas = criar_contas()
    with lock:
        total = sum(conta.saldo for conta in contas)  # cada thread depende do calculo do total, bloqueio só permite acesso ao total após o termino do calculo da thread anterior
    print("Iniciandoo transferências...")

    tarefas = [
        threading.Thread(target=servicos, args=(contas, total)),
        threading.Thread(target=servicos, args=(contas, total)),
        threading.Thread(target=servicos, args=(contas, total)),
        threading.Thread(target=servicos, args=(contas, total)),
        threading.Thread(target=servicos, args=(contas, total)),
        threading.Thread(target=servicos, args=(contas, total))
    ]

    [tarefa.start() for tarefa in tarefas]
    [tarefa.join() for tarefa in tarefas]

    print("Tranferencias completas")
    valida_banco(contas, total)


def servicos(contas, total):
    for _ in range(1, 10_000):
        conta_origem, conta_destino = pega_duas_contas(contas)
        valor = random.randint(1, 100)
        transferir(conta_origem, conta_destino, valor)
        valida_banco(contas, total)


def criar_contas() -> List[Conta]:
    return [
        Conta(saldo=random.randint(5_000, 10_000)),
        Conta(saldo=random.randint(5_000, 10_000)),
        Conta(saldo=random.randint(5_000, 10_000)),
        Conta(saldo=random.randint(5_000, 10_000)),
        Conta(saldo=random.randint(5_000, 10_000)),
        Conta(saldo=random.randint(5_000, 10_000))
    ]


def transferir(conta_origem: Conta, conta_destino: Conta, valor: int):
    # Lock para garantir acesso ao saldo, uma vez que o processo é dependente do saldo
    if conta_origem.saldo < valor:
        return

    with lock:
        conta_origem.saldo -= valor
        time.sleep(0.001)
        conta_destino.saldo += valor


def valida_banco(contas: List[Conta], total: int):
    with lock:
        saldo_atual = sum(conta.saldo for conta in contas)
    if saldo_atual != total:
        print(f"ERRO: Saldo total incorreto: BRL${saldo_atual:.2f} != {total:.2f}", flush=True)
    else:
        print(f"Saldo total: BRL${saldo_atual:.2f}", flush=True)


def pega_duas_contas(contas):
    c1 = random.choice(contas)
    c2 = random.choice(contas)
    while c1 == c2:
        c2 = random.choice(contas)
    return c1, c2


if __name__ == '__main__':
    main()