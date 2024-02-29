import sys


def tail(content, lines=10):
    # Выводит последние 'lines' строк списка строк
    for line in content[-lines:]:
        print(line, end='')


def main():
    # Список файлов для обработки
    files = []

    lines_count = 10  # Количество строк для вывода из файлов
    stdin_lines_count = 17  # Количество строк для вывода из stdin

    if not files:  # Если файлы не переданы, читаем stdin
        print(
            "Введите текст (Ctrl+D для завершения ввода на Linux/Mac, Ctrl+Z на Windows):")
        content = sys.stdin.readlines()
        tail(content, stdin_lines_count)
    else:
        for i, filename in enumerate(files):
            try:
                with open(filename, 'r') as file:
                    content = file.readlines()
                if len(files) > 1:  # Если файлов больше одного, выводим заголовок с именем файла
                    print(f"==> {filename} <==")
                tail(content, lines_count)
                # Добавляем пустую строку между выводами файлов, кроме последнего
                if i < len(files) - 1:
                    print()
            except Exception as e:
                print(f"Ошибка при чтении файла {filename}: {e}")


if __name__ == "__main__":
    main()
