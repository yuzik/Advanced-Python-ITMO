# Функция для добавления текста в документ
def text(content):
    return content

# Функция для создания разделов и подразделов


def section(title, level=1):
    # В зависимости от уровня добавляем 'sub' перед 'section'
    section_type = 'section'
    return '\\' + section_type + '{' + title + '}'

# Функция для создания таблицы


def generate_table(table):
    # Определяем количество столбцов
    num_columns = len(table[0])
    # Строим спецификацию колонок
    column_spec = '|' + ('c|' * num_columns)
    # Начинаем таблицу
    table_string = '\\begin{tabular}{' + column_spec + '}\n\\hline\n'
    # Добавляем строки таблицы
    for row in table:
        row_string = ' & '.join(row) + ' \\\\\n\\hline\n'
        table_string += row_string
    # Заканчиваем таблицу
    table_string += '\\end{tabular}'
    return table_string

# Функция для вставки изображения


def include_graphics(filepath):
    return '\\includegraphics{' + filepath + '}'

# Функция для создания документа


def document(body):
    # Создаем шаблон документа с поддержкой изображений
    doc_template = (
        '\\documentclass{article}\n'
        '\\usepackage{graphicx}\n'  # Добавляем пакет для изображений
        '\\begin{document}\n' +
        body +
        '\n\\end{document}'
    )
    return doc_template


# Функция для сборки документа


def create_document(image_path):
    # Создаем различные части документа
    title = section('Chapter 1', level=1)
    text_content = text('This is an example of text in a LaTeX document.')

    table_data = [
        ["Title 1", "Title 2"],
        ["Text 1", "Text 2"],
        ["Text 3", "Text 4"]
    ]
    table = generate_table(table_data)

    # Вставляем изображение, используя предоставленный путь
    image = include_graphics(image_path)  # Использование аргумента функции

    # Собираем все части в один документ
    body_elements = [title, text_content,
                     table, image]  # Добавление изображения
    body = '\n\n'.join(body_elements)
    return document(body)


# Генерируем документ и сохраняем в файл
image_path = 'img/cloud.png'
latex_code = create_document(image_path)
filename = "artifacts/2_1.tex"
with open(filename, "w") as file:
    file.write(latex_code)
print(f"LaTeX document has been saved to: {filename}")
