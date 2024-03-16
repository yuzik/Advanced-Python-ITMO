from latex_generator import create_document
import subprocess

# Функция для генерации LaTeX документа и генерации в PDF


def generate_and_compile_latex(image_path):
    # Генерация LaTeX кода
    latex_code = create_document(image_path)

    # Запись в файл
    tex_filename = "artifacts/2_2.tex"
    with open(tex_filename, "w") as f:
        f.write(latex_code)
    print(f"LaTeX код сохранен в {tex_filename}")

    # Генерация в PDF
    compile_latex_to_pdf(tex_filename)

# Функция генерации документа в PDF


def compile_latex_to_pdf(tex_file):
    print(f"Создаем {tex_file} PDF...")
    process = subprocess.run(['pdflatex', tex_file],
                             capture_output=True, text=True)

    if process.returncode == 0:
        print("Успешно.")
    else:
        print("Ошибка:")
        print(process.stderr)


# Путь к изображению
image_path = "img/cloud.png"

# Запуск
generate_and_compile_latex(image_path)
