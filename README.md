<h1>Отправляем уведомления о проверке работ</h1>

Отпраляем в телеграм уведомление о проверке работ на сервисе DVMN.org



<h2>Подготовка к работе</h2>

1. Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
   
   ``` pip install -r requirements.txt ```

2. Создать внутри репозитория файл .env и указать следудующие параметры:
   ```
   TOKEN_TG=***
   TOKEN_DEVMAN=***
   ```
   Описание:
    
   <b>TOKEN_TG - Уникальный токен вашего канала телеграмм<br>
   <b>TOKEN_DEVMAN</b> - Уникальный токен сервиса DVMN.org(Можно получить на сайте DVMN.org) <br>
   
<h2>Описание работы</h2>

Для запуска скрипта необходимо через агументы команднной строки (-ID) передать ID чата в телеграмм<br>
Пример: 
```
python bot.py -id 111111
```
Бот будет запущен и при изменении статуса вашей работы вы получить уведомление!

<b>!!! Незабудьте указать переменные окружения в файле .env</b>


<h1>Цель проекта</h1>

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.


