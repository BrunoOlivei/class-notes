# Step 1
import threading
import time


def main():
    # Step 2
    th = threading.Thread(target=count_bolsonaros_crimes, args=('Bolsonaro Corruption', 10))

    # Step 3
    th.start()  # Adds the thread to the ready-to-run thread pool

    print('I can pause in the militancy....')
    print('...' * 10)

    # Step 4
    th.join() # Wait for the thread to finish

    print("That's all Folks, for now!")


def count_bolsonaros_crimes(crime, number):
    for i in range(1, number + 1):
        print(f'{i} {crime}...')
        time.sleep(1)


if __name__ == '__main__':
    main()
