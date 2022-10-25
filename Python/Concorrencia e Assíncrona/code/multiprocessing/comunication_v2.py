import multiprocessing


def ping(queue):
    """
    Envia a mensagem para o processo pong
    :param queue:
    :return:
    """
    queue.put('ping')


def pong(queue):
    """
    Recebe a mensagem do processo ping e imprime a mensagem recebida
    :param queue:
    :return:
    """
    msg = queue.get()
    print(msg)


def main():
    """
    Cria um processo pong e um processo ping
    :return:
    """
    queue = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=ping, args=(queue,))
    p2 = multiprocessing.Process(target=pong, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    main()
    print("Fim")

# Compare this snippet from multiprocessing\comunication_v1.py:

# O método Pipe cria a comunicação entre os processos, porém não permite bloquear a comunicação entre eles.
# Para isso, utiliza-se o Queue.
# Queue é uma fila de mensagens que permite a comunicação entre os processos.
