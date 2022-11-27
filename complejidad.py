import time
import sys
import threading


threading.stack_size(134217728)

sys.setrecursionlimit(210000)


def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1
    return respuesta


def factorial_r(n):

    if n == 1:
        return 1
    return n * factorial_r(n-1)


def main():

    n = 200000

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final-comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final-comienzo)


if __name__ == "__main__":
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

