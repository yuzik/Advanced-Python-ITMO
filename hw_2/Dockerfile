# Используем базовый образ Python
FROM python:3.9

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y \
    texlive \
    texlive-latex-extra \
    texlive-fonts-recommended

# Копируем исходный код в контейнер
COPY . /app
WORKDIR /app

# Устанавливаем зависимости Python
RUN pip install -r requirements.txt

# Команда для запуска скрипта при запуске контейнера
CMD ["python", "main_2_3.py"]
