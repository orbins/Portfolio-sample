# [Portfolio-sample - шаблон для портфолио](https://github.com/orbins/Portfolio-sample) 

Это мой первый проект - шаблон сайта-портфолио\
За основу был взят один из полу-готовых frontend-шаблонов, \
он был переработан и для него был реализован полноценный backend так, 
чтобы можно было разместить свои проекты и получать сообщения от посетителей.


## 🛠️ Установка и запуск

Для запуска приложения должен быть установлен [git](https://git-scm.com/) и [docker](https://www.docker.com/).

```bash
git clone https://github.com/orbins/Portfolio-sample.git
cd Portfolio-sample
```

Шаблон для создания .env файла (содержит необходимые для работы перменные окружения). Данный файл должен находится во вложенной папке `main` проекта:
```env
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'ваша почта'
EMAIL_HOST_PASSWORD = 'пароль для внешних приложений от почты'
TO_EMAIL = 'ваша почта или почта на которую необходимо отправлять сообщения с сайта'
```

Собрать и запустить контейнер
```bash
cd 
sudo docker build . -t portfolio
sudo docker run -p 8000:8000 -d --rm portfolio
```

Панель администратора

- логин: `admin`
- пароль: `1234`
----


## ⚙️ Использованные технологии

- [Python 3.9](https://www.python.org/)
- [Django 4.1](https://www.djangoproject.com/)
- [Docker](https://docker.com/)

## 🧑‍💻 Автор

- [Ткаченко Данил](https://www.github.com/orbins)

<p align="right"><a href="#top">⬆️ Наверх</a></p>