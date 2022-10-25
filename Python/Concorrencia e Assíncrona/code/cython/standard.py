import datetime
import math


def main():
    begin = datetime.datetime.now()
    compute(end=50_000_000)

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
Tempo de execução: 14.35 segundos
"""