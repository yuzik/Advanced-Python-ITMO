import multiprocessing
import time
import codecs
from multiprocessing import Queue, Process


def process_a(input_queue, output_queue):
    while True:
        message = input_queue.get()
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        with open('interaction_log.txt', 'a') as log_file:
            log_file.write(f"{timestamp} - Process A received: {message}\n")
        if message == "STOP":
            output_queue.put("STOP")
            break
        lower_message = message.lower()
        time.sleep(5)
        output_queue.put(lower_message)
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        with open('interaction_log.txt', 'a') as log_file:
            log_file.write(
                f"{timestamp} - Process A processed and sent: {lower_message}\n")


def process_b(input_queue, output_queue):
    while True:
        message = input_queue.get()
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        with open('interaction_log.txt', 'a') as log_file:
            log_file.write(f"{timestamp} - Process B received: {message}\n")
        if message == "STOP":
            break
        rot13_message = codecs.encode(message, 'rot_13')
        print(f"{timestamp} - Process B: {rot13_message}")
        output_queue.put(rot13_message)
        with open('interaction_log.txt', 'a') as log_file:
            log_file.write(
                f"{timestamp} - Process B processed and sent: {rot13_message}\n")


if __name__ == "__main__":
    input_queue_a = Queue()
    queue_ab = Queue()
    queue_b_main = Queue()

    process_a_instance = Process(
        target=process_a, args=(input_queue_a, queue_ab))
    process_b_instance = Process(
        target=process_b, args=(queue_ab, queue_b_main))

    process_a_instance.start()
    process_b_instance.start()

    print("Type your messages. Type 'STOP' to end.")

    with open('interaction_log.txt', 'w') as log_file:
        log_file.write("Interaction Log\n")
        log_file.write("================\n")

    while True:
        user_input = input()
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        input_queue_a.put(user_input)
        with open('interaction_log.txt', 'a') as log_file:
            log_file.write(f"{timestamp} - Main Process sent: {user_input}\n")
        if user_input == "STOP":
            break

        response = queue_b_main.get()
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        print(f"{timestamp} - Main Process received: {response}")
        with open('artifacts/4_3.txt', 'a') as log_file:
            log_file.write(
                f"{timestamp} - Main Process received: {response}\n")

    process_a_instance.join()
    process_b_instance.join()
