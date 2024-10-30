FROM python:3.10

# Установка зависимостей для psycopg2 и Pillow
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    python3-dev \
    musl-dev \
    libjpeg-dev \
    zlib1g-dev

# Установка рабочей директории
WORKDIR /app

# Копирование файлов в контейнер
COPY . /app

# Установка зависимостей проекта
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Экспорт переменных среды
ENV PYTHONUNBUFFERED=1

# Запуск сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
