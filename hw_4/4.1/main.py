from threading import Thread
from multiprocessing import Process, Pool
import time


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# Функция записи в файл


def write_to_file(data):
    with open("artifacts/4_1.txt", "a") as file:
        file.write(data + "\n")


def run_sync(n):
    start_time = time.time()
    results = [fib(n) for _ in range(10)]
    end_time = time.time()
    write_to_file(f"Sync: {end_time - start_time} s.")


def run_threading(n):
    threads = []
    start_time = time.time()
    for i in range(10):
        thread = Thread(target=fib, args=(n,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    write_to_file(f"Threading: {end_time - start_time} s.")


def run_multiprocessing(n):
    start_time = time.time()
    with Pool(10) as p:
        p.map(fib, [n] * 10)
    end_time = time.time()
    write_to_file(f"Multiprocessing: {end_time - start_time} s.")


if __name__ == "__main__":
    # Очистка файла результатов перед записью новых результатов
    open("artifacts/4_1.txt", "w").close()

    n = 35
    print("Запускаем вычисление Фибоначи для n =", n)

    run_sync(n)  # Синхронный запуск
    run_threading(n)  # Многопоточный запуск
    run_multiprocessing(n)  # Многопроцессный запуск
