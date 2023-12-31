# RegistrationConferenceBot
______
**RegistrationConferenceBot** - это специальный бот для регистрации на абстрактную конференцию
через сервис vk.com. 
Это мой pet project, созданный для изучения программирования и computer science, отработки навыков
работы с языком программирования, работы с API, с сетевыми запросами, базами данных и другими библиотеками.

## Используемые технологии
___________

![version](https://img.shields.io/badge/python-3.11-blue)


![package](https://img.shields.io/badge/vk--api-11.9.9-violet)
![package](https://img.shields.io/badge/requests-2.31.0-violet)
![package](https://img.shields.io/badge/Pillow-10.0.0-violet)
![package](https://img.shields.io/badge/pony.orm-0.7.16-violet)

![package](https://img.shields.io/badge/PostgreSQL-red)

![license](https://img.shields.io/badge/license-Apache__License__V2.0-green)

В проекте используется объектно-ориентированного программирования (ООП), 
работа с API сервисами, ведение базы данных, логирование действий, работа с изображениями, 
регулярные выражения, работа с сетевыми запросами, тестирование.


## Взаимодействие с пользователем:
____________

Этот бот моделирует сценарий регистрации пользователя на конференцию, ведя
диалог с пользователем по заготовленным шаблонам. При просьбе бота "зарегистрировать",
начинается заготовленный сценарий при котором у пользователя запрашивают его имя и email, 
после чего эти данные будут занесены в
базу данных, а самому пользователю будет отправлен сгенерированное изображение с его данными 
и персональным аватаром.

## Установка и запуск
___________

Для установки данной программы нужно скачать репозиторий со всеми файлами с GitHub.
Создать виртуальное окружение, но можно использовать и коренную папку, далее загрузить
туда все необходимые пакеты с помощью команды: 
``` python
pip install -r requirements.txt
```
После этого необходимо создать файл settings.py, в который нужно перенести 
все данные из файла settings.py.default и обязательно нужно указать в нем
персональный [TOKEN](https://clck.ru/35FbAK) и GROUP_ID!

После всего этого можно запускать файл `bot.py` и начинать диалог с ботом. 

## Лицензия
___________

Проект разработан с использованием лицензии [Apache License, Version 2.0](https://opensource.org/license/apache-2-0/)