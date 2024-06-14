import threading
import time


def output_numbers():
    for number in range(1, 11):
        print(number)
        time.sleep(1)


def output_letters():
    for letter in ('abcdifghij'):
        print(letter)
        time.sleep(1)


thread_numbers = threading.Thread(target=output_numbers)
thread_letters = threading.Thread(target=output_letters)

thread_numbers.start()
thread_letters.start()

thread_numbers.join()
thread_letters.join()


