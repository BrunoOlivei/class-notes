from typing import Generator


def fibonacci() -> Generator[int, None, None]:
    valor: int = 0
    proximo: int = 1
    while True:
        valor, proximo = proximo, valor + proximo
        yield valor


if __name__ == '__main__':
    for n in fibonacci():
        print(n, end=", ")
        if n > 100:
            break

    print("\nPronto")
