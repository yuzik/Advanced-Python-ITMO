import math
import time
import logging
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# Настройка логирования
logging.basicConfig(filename='artifacts/4_2.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')


def integrate_part(f, start, end, step):
    acc = 0
    x = start
    while x < end:
        acc += f(x) * step
        x += step
    return acc


def integrate(f, a, b, *, n_jobs=1, n_iter=10000000, executor_class=ThreadPoolExecutor):
    step = (b - a) / n_iter
    part_size = n_iter // n_jobs
    futures = []

    with executor_class(max_workers=n_jobs) as executor:
        for i in range(n_jobs):
            start = a + i * part_size * step
            end = start + part_size * step
            logging.info(f"Запуск задачи {i+1} для диапазона ({start}, {end})")
            futures.append(executor.submit(
                integrate_part, f, start, end, step))

        result = sum(f.result() for f in futures)

    return result


def measure_time_and_log(n_jobs, executor_class):
    start_time = time.time()
    result = integrate(math.cos, 0, math.pi / 2,
                       n_jobs=n_jobs, executor_class=executor_class)
    end_time = time.time()
    elapsed_time = end_time - start_time
    logging.info(f"{executor_class.__name__} с {n_jobs} воркерами завершен за {
                 elapsed_time:.2f} секунд. Результат: {result}")
    return elapsed_time


if __name__ == '__main__':
    import multiprocessing

    cpu_count = multiprocessing.cpu_count()
    n_jobs_list = range(1, cpu_count * 2 + 1)

    thread_times = []
    process_times = []

    for n_jobs in n_jobs_list:
        thread_time = measure_time_and_log(n_jobs, ThreadPoolExecutor)
        thread_times.append((n_jobs, thread_time))
        process_time = measure_time_and_log(n_jobs, ProcessPoolExecutor)
        process_times.append((n_jobs, process_time))

    with open('artifacts/comparison.txt', 'w') as file:
        file.write("ThreadPoolExecutor times:\n")
        for n_jobs, time in thread_times:
            file.write(f"{n_jobs} workers: {time:.2f} seconds\n")

        file.write("\nProcessPoolExecutor times:\n")
        for n_jobs, time in process_times:
            file.write(f"{n_jobs} workers: {time:.2f} seconds\n")

    print("Результаты записаны в comparison.txt")
