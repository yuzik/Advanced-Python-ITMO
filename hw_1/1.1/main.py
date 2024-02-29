import sys


def print_numbered_lines(source):
    line_number = 1
    for line in source:
        # `end=''` чтобы избежать добавления дополнительной новой строки
        print(f"{line_number}\t{line}", end='')
        line_number += 1


if __name__ == "__main__":
    file_name = '/Users/yuzik/Edu/php/hw_1/1.1/file.txt'
    try:
        with open(file_name, 'r') as file:
            print_numbered_lines(file)
    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")
