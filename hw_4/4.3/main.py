from multiprocessing import Process, Queue, Pipe
import time
import codecs


def process_a(queue_from_main, queue_to_b):
    while True:
        msg = queue_from_main.get()  # Сообщения от процесса A
        if msg == "exit":
            queue_to_b.put(msg)
            break
        msg_lower = msg.lower()  # Сообщения в нижний регистр
        time.sleep(5)
        queue_to_b.put(msg_lower)  # Сообщения в процесс B


def process_b(queue_from_a, conn_to_main):
    while True:
        msg = queue_from_a.get()
        if msg == "exit":
            break
        msg_rot13 = codecs.encode(msg, 'rot_13')  # Применение ROT13
        conn_to_main.send(msg_rot13)  # Сообщения обратно в процесс


def log_interaction(message):
    with open("artifacts/4_3.txt", "a") as log_file:
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        log_file.write(f"[{current_time}] {message}\n")


if __name__ == "__main__":
    # Очередь для сообщений
    queue_main_to_a = Queue()
    queue_a_to_b = Queue()
    parent_conn, child_conn = Pipe()

    p_a = Process(target=process_a, args=(queue_main_to_a, queue_a_to_b))
    p_b = Process(target=process_b, args=(queue_a_to_b, child_conn))
    p_a.start()
    p_b.start()

    try:
        while True:
            user_input = input("Введите 'exit' для выхода: ")

            log_interaction(f"Отправлено: {user_input}")          # Логирование
            queue_main_to_a.put(user_input)
            if user_input == "exit":
                break
            received_msg = parent_conn.recv()
            log_interaction(f"Получено: {received_msg}")
            print(f"Обработанное сообщение: {received_msg}")
    finally:
        p_a.join()
        p_b.join()
        print("Завершение")
