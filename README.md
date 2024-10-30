
# Image API Project - shakalizator

## Функциональные возможности
- **Регистрация и аутентификация пользователей** с использованием JWT токенов
- **Загрузка изображений** с сохранением информации о размере и разрешении, при загрузке изображение становится черно-белым, а разрешение меняется на 100х100 пикселей
- **Получение списка изображений** с возможностью детального просмотра по ID
- **Преобразование изображений** (например, в черно-белое)
- **Удаление изображений** по ID

## Структура проекта

```bash
project-root/
│
├── images/                   # Приложение для управления изображениями
│   ├── migrations/           # Миграции базы данных
│   ├── models.py             # Определение модели Image
│   ├── serializers.py        # Сериализаторы для Image
│   ├── views.py              # API-контроллеры для CRUD-операций
│   ├── urls.py               # URL-маршруты приложения
│   └── tests.py              # Unit-тесты для API
│
├── images_api/             # Основная конфигурация Django
│   ├── settings.py           # Настройки проекта
│   ├── urls.py               # Основные маршруты API
│   └── wsgi.py               # Точка входа для сервера
│
├── requirements.txt          # Список зависимостей
├── manage.py                 # Django скрипт управления проектом
└── README.md                 # Документация проекта
```
## Запуск контейнеров
В проекте два контейнера - для wtb-приложения django и приложения images.
```
docker-compose up --build
```
## Ручная установка и настройка

### Установка зависимостей
```bash
python3 -m venv venv
source venv/bin/activate  # для Windows используйте `venv\Scripts\activate`
pip install -r requirements.txt
```

### Настройка базы данных
Проект использует PostgreSQL. Настройте подключение в `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'image_api_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Применение миграций
```bash
python manage.py migrate
```

### Создание суперпользователя
```bash
python manage.py createsuperuser
```

### Запуск сервера
```bash
python manage.py runserver
```

## Тестирование

Для запуска unit-тестов используйте команду:
```bash
python manage.py test
```

## Документация API
Документация Swagger доступна по адресу: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)  
Документация ReDoc доступна по адресу: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

## Примеры API-запросов

### Регистрация и аутентификация
- **POST /api/auth/register/** - регистрация нового пользователя
- **POST /api/auth/login/** - получение JWT токена

### Работа с изображениями
- **POST /api/images/** - загрузка изображения
- **GET /api/images/** - получение списка изображений
- **GET /api/images/{id}/** - получение изображения по ID
- **DELETE /api/images/{id}/** - удаление изображения по ID

## Дополнительная информация
Проект включает поддержку Swagger для автоматической генерации API-документации. Реализованы unit-тесты для ключевых функций API. API защищен JWT-токенами для безопасности пользовательских данных. Также в качестве брокера используется RabbitMQ в связке с Celery.
