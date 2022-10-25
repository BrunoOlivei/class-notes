import datetime
import math

import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor as Executor


def main():
    qtd_cores = multiprocessing.cpu_count()
    print(f"Realizando o processamento matemático com {qtd_cores} cores")

    begin = datetime.datetime.now()

    with Executor(max_workers=qtd_cores) as executor:
        for n in range(1, qtd_cores):
            ini = 50_000_000 * (n - 1) / qtd_cores
            fim = 50_000_000 * n / qtd_cores
            print(f'Core {n}: ini={ini:.2f} fim={fim:.2f}')
            executor.submit(compute, end=fim, begin=ini)

    duration = datetime.datetime.now() - begin

    print(f'Tempo de execução: {duration.total_seconds():.2f} segundos')


def compute(end, begin=1):
    pos = begin
    fator = 1000 * 1000
    while pos < end:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))


if __name__ == '__main__':
    main()


"""
Tempo de execução: 5.35 segundos
"""