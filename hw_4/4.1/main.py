import time
import threading
import multiprocessing


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def measure_sync_execution(n, repetitions):
    start_time = time.time()
    for _ in range(repetitions):
        fibonacci(n)
    end_time = time.time()
    return end_time - start_time


def fibonacci_worker(n, result, index):
    result[index] = fibonacci(n)


def measure_threaded_execution(n, repetitions):
    threads = []
    result = [None] * repetitions
    start_time = time.time()
    for i in range(repetitions):
        thread = threading.Thread(target=fibonacci_worker, args=(n, result, i))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    return end_time - start_time


def fibonacci_process_worker(n, result, index):
    result[index] = fibonacci(n)


def measure_multiprocessed_execution(n, repetitions):
    processes = []
    with multiprocessing.Manager() as manager:
        result = manager.list([None] * repetitions)
        start_time = time.time()
        for i in range(repetitions):
            process = multiprocessing.Process(
                target=fibonacci_process_worker, args=(n, result, i))
            processes.append(process)
            process.start()
        for process in processes:
            process.join()
        end_time = time.time()
    return end_time - start_time


if __name__ == '__main__':
    n = 35
    repetitions = 10

    sync_time = measure_sync_execution(n, repetitions)
    threaded_time = measure_threaded_execution(n, repetitions)
    multiprocessed_time = measure_multiprocessed_execution(n, repetitions)

    result = (
        f"Синхронное выполнение: {sync_time:.2f} секунд\n"
        f"Выполнение с использованием потоков: {threaded_time:.2f} секунд\n"
        f"Выполнение с использованием процессов: {multiprocessed_time:.2f} секунд\n"
    )

    with open("artifacts/4_1.txt", "w") as file:
        file.write(result)

    print("Результаты записаны в execution_times.txt")
