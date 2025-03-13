# Django проект, который при вызове "/get-current-usd/" возвращает актуальный курс доллара к рублю в формате JSON и 10 последних запросов курсов

## Для получения курса использовано внешнее API https://www.exchangerate-api.com/.
## Между каждым запросом курса пауза не менее 10 секунд.

# Инструкция по запуску проекта
* Скачать исходный код проекта: `git clone https://github.com/Jaguar56/Test_project.git`
* Перейти в папку с проектом: `cd Test_project/`
* Установить виртуальное окружение: `python -m pip install --upgrade pip && pip install virtualenv`
* Создать виртуальное окружение `python -m virtualenv django_venv`
* Активировать виртуальное окружение:
1. Для OS Windows  `django_venv\Scripts\activate`
2. Для OS Linux `source django_venv/bin/activate`
* Установить зависимости: `pip install -r requirements.txt`
* Запустить сервер `python manage.py runserver`

## Использование

После запуска перейти по ссылке
URL: [http://127.0.0.1:8000/get-current-usd/](http://127.0.0.1:8000/get-current-usd/).

## Тайминги

Компонент	                 Первичная оценка	      Фактическое время

Настройка проекта	         30 мин	                  20 мин

Модель и миграции	         20 мин	                  15 мин

Логика запросов к API	     2 часа	                  3 часа

Эндпоинт и сериализация	     1 час	                  1 час

Тестирование	             1 час	                  1.5 часа

Итого:	                     5 часов	              6.5 часов
