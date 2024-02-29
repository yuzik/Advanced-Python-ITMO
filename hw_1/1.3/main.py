import sys


def wc(file_paths):
    total_lines, total_words, total_bytes = 0, 0, 0
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                lines = content.count('\n')
                words = len(content.split())
                bytes_ = len(content.encode('utf-8'))
                print(f"{lines} {words} {bytes_} {file_path}")
                total_lines += lines
                total_words += words
                total_bytes += bytes_
        except Exception as e:
            print(f"Ошибка при чтении файла {file_path}: {e}")

    if len(file_paths) > 1:
        print(f"{total_lines} {total_words} {total_bytes} total")


def read_from_stdin():
    print("Введите текст (Ctrl+D для завершения ввода на Linux/Mac, Ctrl+Z на Windows):")
    content = sys.stdin.read()
    lines = content.count('\n')
    words = len(content.split())
    bytes_ = len(content.encode('utf-8'))
    print(f"{lines} {words} {bytes_}")


def main():
    # Получаем список файлов из аргументов командной строки
    file_paths = sys.argv[1:]

    if not file_paths:
        read_from_stdin()
    else:
        wc(file_paths)


if __name__ == "__main__":
    main()
