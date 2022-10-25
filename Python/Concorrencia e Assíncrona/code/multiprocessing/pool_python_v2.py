import multiprocessing


def calcular(dado, multiplicador):
    return dado ** multiplicador


def imprimir_nome_processo():
    print(f'Iniciando o processo com nome: {multiprocessing.current_process().name}')


def main():
    tamanho_pool = multiprocessing.cpu_count() * 2  # 3 * 2 -> 6 processos

    pool = multiprocessing.Pool(processes=tamanho_pool, initializer=imprimir_nome_processo)

    entradas = list(range(7))
    saidas = pool.map(calcular, entradas, 2)

    print(saidas)

    pool.close()  # Dá um aviso para o pool que não vai mais enviar mais dados para os processos e espera que os processos terminem
    pool.join()


if __name__ == "__main__":
    main()
    print("Fim")