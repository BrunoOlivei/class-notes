import time
import colorama
from threading import Thread
from queue import Queue


def get_data(queue):
    for i in range(1, 11):
        print(colorama.Fore.GREEN + f"Dados {i} gerado.", flush=True)
        time.sleep(2)
        queue.put(i)


def process_data(queue):
    while queue.qsize() > 0:
        data = queue.get()
        print(colorama.Fore.RED + f"Dados {data * 2} processado.", flush=True)
        time.sleep(1)
        queue.task_done()


if __name__ == '__main__':
    print(colorama.Fore.WHITE + "Sistema iniciando.", flush=True)
    queue = Queue()
    th1 = Thread(target=get_data, args=(queue,))
    th2 = Thread(target=process_data, args=(queue,))

    th1.start()
    th1.join()

    th2.start()
    th2.join()
