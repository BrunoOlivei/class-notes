import datetime
import computa


def main():
    begin = datetime.datetime.now()
    computa.compute(end=50_000_000)

    duration = datetime.datetime.now() - begin

    print(f'Tempo de execução: {duration.total_seconds():.4f} segundos')


if __name__ == '__main__':
    main()


"""
Tempo de execução: 22.13 segundos
Tempo de execução: 18.32 segundos
Tempo de execução: 0.00 segundos
Tempo de execução: 0.0000 segundos
"""