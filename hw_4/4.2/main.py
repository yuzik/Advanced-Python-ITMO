import math
import concurrent.futures
import time
import logging
import os

# Настройка логирования
logging.basicConfig(filename='artifacts/4_2.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def integrate(f, a, b, *, n_jobs=1, n_iter=10000000):
    step = (b - a) / n_iter
    total_sum = 0
    part_iter = n_iter // n_jobs
    futures = []

    def integrate_part(start, end):
        acc = 0
        for i in range(start, end):
            acc += f(a + i * step) * step
        return acc

    with concurrent.futures.ThreadPoolExecutor(max_workers=n_jobs) as executor:
        for i in range(n_jobs):
            start = i * part_iter
            end = start + part_iter if i < n_jobs - 1 else n_iter
            futures.append(executor.submit(integrate_part, start, end))
            logging.info(f'Task {i+1} started.')

    for future in concurrent.futures.as_completed(futures):
        total_sum += future.result()

    return total_sum


def run_experiments():
    cpu_count = os.cpu_count() or 1
    for executor_class in [concurrent.futures.ThreadPoolExecutor, concurrent.futures.ProcessPoolExecutor]:
        with open(f'artifacts//comparison_{executor_class.__name__}.txt', 'w') as file:
            for n_jobs in range(1, cpu_count * 2 + 1):
                start_time = time.time()
                result = integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs)
                elapsed_time = time.time() - start_time
                logging.info(
                    f'{executor_class.__name__} - n_jobs: {n_jobs}, Time: {elapsed_time}, Result: {result}')
                file.write(f'n_jobs: {n_jobs}, Time: {elapsed_time}s\n')


if __name__ == "__main__":
    run_experiments()
