<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Project</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/sameanonim/project/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/sameanonim/project/pulls)

</div>

---

<p align="center"> В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек. Заказчик прочитал книгу, впечатлился и обратился к вам с запросом реализовать трекер полезных привычек. В рамках учебного проекта реализована бэкенд-часть SPA веб-приложения.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)

## 🧐 About <a name = "about"></a>

В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек. Заказчик прочитал книгу, впечатлился и обратился к вам с запросом реализовать трекер полезных привычек. В рамках учебного проекта реализована бэкенд-часть SPA веб-приложения.

## 🏁 Getting Started <a name = "getting_started"></a>

Клонировать проект,

```
$ git clone https://github.com/sameanonim/project.git 
```
Создать и активировать виртуальное окружение

```
$ python3 -m venv venv
```
Установить зависимости

```
pip install -r requirements.txt
```

### Prerequisites

What things you need to install the software and how to install them.

```
- PostgreSQL
- Redis
```

### Installing

Запустить миграцию.

```
python manage.py migrate
```

Загрузка начальных данных (сгенерированы автоматически с помощью https://mockaroo.com/)

```
python manage.py loaddata db.json
```

Запустить сервер

```
python manage.py runserver
```

Создание периодической задачи
```
python manage.py add_tasks
```

Запуск Celery
```
celery -A config worker -l INFO -P eventlet
```

Запуск celery-beat
```
celery -A config worker --loglevel=info
```

## 🔧 Running the tests <a name = "tests"></a>

```
python manage.py test
```

Покрытие тестами

```
coverage run --source='.' manage.py test
```

```
coverage report
```

## 🚀 Deployment <a name = "deployment"></a>

Создать файл .env.docker, прописать в нём настройки.

## Сборка образа и запуск в доке

docker-compose up -d -build