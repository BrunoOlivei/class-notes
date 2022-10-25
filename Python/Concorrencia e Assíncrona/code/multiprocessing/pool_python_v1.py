import multiprocessing


def calcular(dado):
    return dado ** 2


def main():
    tamanho_pool = multiprocessing.cpu_count() * 2  # 3 * 2 -> 6 processos

    pool = multiprocessing.Pool(processes=tamanho_pool)

    entradas = list(range(7))
    saidas = pool.map(calcular, entradas)

    print(saidas)

    pool.close()  # Dá um aviso para o pool que não vai mais enviar mais dados para os processos e espera que os processos terminem
    pool.join()


if __name__ == "__main__":
    main()
    print("Fim")