# Django Commerce Hub
Тестовое задание от компании "ООО Простые решения"

Выполнен весь основной функционал, а так же бонусы:

· 	Запуск используя Docker 

· 	Использование environment variables 

· 	Просмотр Django Моделей в Django Admin панели 

Основные запросы начинаются c "api". То есть: api/buy/{id}, api/item/{id}

Приложение помещается в контейнер с помощью Docker и управляется с помощью Docker Compose.

## Использование

Для начала создайте объекты `Item`.

- Используйте `/api/item/{id}` чтобы перейти на страничку с товаром.
- Нажмите кнопку `buy` чтобы пеейти к оплате товара.

- Используйте `/api/buy/{id}` чтобы получить session id.

## Запуск

Для начала нужно создать файл `.env` и положить туда api ключи от Stripe.


1. Скопируйте репозиторий:

     ```bash
     git clone https://github.com/geoCrock/Django-Commerece-Hub.git
     ```

2. Войдите в корень проекта:

     ```bash
     cd djangocommercehub
     ```

3. Установите зависимости:

  ```bash
  pip install -r requirements.txt
  ```

4. Создайте `.env` и положите туда ваши API ключи от Stripe:

    Example:
     ```env
     STRIPE_API_KEY_PRIVATE = "STRIPE_API_KEY_PRIVATE"
    
     STRIPE_API_KEY_PUBLIC = "STRIPE_API_KEY_PUBLIC"
     ```


5. Сделайте миграции и запустите проект:
   
    ```bash
     python manage.py makemigrations
     ```

    ```bash
     python manage.py migrate
     ```

    ```bash
     python manage.py runserver
     ```
   
7. Приложение доступно на http://127.0.0.0:8000.



##  Запуск через Docker

Убедитесь, что в вашей системе установлены следующие компоненты:

- Docker
- Docker Compose


1. Скопируйте репозиторий:

     ```bash
     git clone https://github.com/geoCrock/Django-Commerece-Hub.git
     ```

2. Войдите в корень проекта:

     ```bash
     cd djangocommercehub
     ```

3. Установите зависимости:

  ```bash
  pip install -r requirements.txt
  ```

4. Создайте `.env` и положите туда ваши API ключи от Stripe:

    Example:
     ```env
     STRIPE_API_KEY_PRIVATE = "STRIPE_API_KEY_PRIVATE"
    
     STRIPE_API_KEY_PUBLIC = "STRIPE_API_KEY_PUBLIC"
     ```
  
5. Создайте и запустите контейнеры Docker:

     ```bash
     docker-compose up --build
     ```
     
