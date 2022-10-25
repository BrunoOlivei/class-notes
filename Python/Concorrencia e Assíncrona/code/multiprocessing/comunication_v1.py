import multiprocessing


def ping(conn):
    """
    Envia a mensagem para o processo pong
    :param conn:
    :return:
    """
    conn.send('ping')
    msg = conn.recv()
    print(msg)


def pong(conn):
    """
    Recebe a mensagem do processo ping e imprime a mensagem recebida
    :param conn:
    :return:
    """
    msg = conn.recv()
    print(msg)
    conn.send('pong')


def main():
    """
    Cria um processo pong e um processo ping
    :return:
    """
    conn1, conn2 = multiprocessing.Pipe(True)  # Cria um pipe para comunicação entre os processos

    p1 = multiprocessing.Process(target=ping, args=(conn1,))
    p2 = multiprocessing.Process(target=pong, args=(conn2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    main()
    print("Fim")

# Compare this snippet from multiprocessing\comunication_v2.py:

# O método Pipe cria a comunicação entre os processos, porém não permite bloquear a comunicação entre eles.
# Para isso, utiliza-se o Queue.
# Queue é uma fila de mensagens que permite a comunicação entre os processos.
