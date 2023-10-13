# tst_ut_dj
Тестовое задание.

## Установка
1. Склонируйте проект
```bash
git clone https://github.com/rastal88/tst_ut_dj.git
cd test_ut_dj
```
2. Установка
Установите и активируйте виртуальное окружение
```bash
python -m venv venv
```
```bash
source venv/bin/activate
```
Установите зависимости
```bash
pip install -r requirements.txt
```
3.Запуск
Перейдите в дерикторию с файлом manage.py
Проведите миграции
```bash
python manage.py migrate
```
Создаете суперпользователя(введите имя и пороль)
```bash
python manage.py createsuperuser
```

Далее используйте команду
```bash
python manage.py ranserver
```
Введите в браузере http://127.0.0.1:8000/admin и зайдите в админ-панель. 
Добавьте меню согласно вашим требованиям и проверьте работу на главной странице сайта : http://127.0.0.1:8000

## Условия тестового задания
Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6 )Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8)На отрисовку каждого меню требуется ровно 1 запрос к БД
 Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
 {% draw_menu 'main_menu' %}
 При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.



