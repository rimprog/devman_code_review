# Пример работы с API Evernote

В данном проекте реализуется пример работы с [API](https://dev.evernote.com/doc/start/python.php) сервиса заметок ["Evernote"](https://www.evernote.com/).

Проект представляет собой набор из трех скриптов, позволяющих реализовать возможности API Evernote.

## Подготовка к запуску проекта

Пройдите процедуру получения необходимых для работы проекта токенов:
1. Получите [Evernote API key](https://dev.evernote.com/#apikey).
2. [Активируйте (Activate an API Key)](https://dev.evernote.com/support/) полученный в предыдущем шаге ключ, для работы на production серверах Evernote.
3. Создайте, либо используйте уже существующий аккаунт [Evernote](https://www.evernote.com/), чтобы [получить oauth_token аккаунта](https://dev.evernote.com/doc/articles/authentication.php), для использования API Evernote от имени аккаунта.

Создайте в корневой папке проекта файл `.env` и поместите внутрь все полученные в предыдущих шагах токены.
Получите также GUID шаблона заметки (Note) с которой будете работать, GUID блокнота (Notebook), а также GUID блокнота "Входящие"(Inbox Notebook).
Подробнее про GUID вы можете прочитать [ЗДЕСЬ](https://dev.evernote.com/doc/articles/core_concepts.php). Структуру URL адреса заметки и журнала с содержанием GUID, вы можете найти [ЗДЕСЬ](https://dev.evernote.com/doc/articles/sharing.php).

Пример `.env`:
```
EVERNOTE_CONSUMER_KEY=YOUR_EVERNOTE_API_CONSUMER_KEY
EVERNOTE_CONSUMER_SECRET=YOUR_EVERNOTE_API_SECRET_KEY
EVERNOTE_PERSONAL_TOKEN=YOUR_EVERNOTE_OAUTH_TOKEN

JOURNAL_TEMPLATE_NOTE_GUID=YOUR_TEMPLATE_NOTE_GUID
JOURNAL_NOTEBOOK_GUID=YOUR_NOTEBOOK_GUID

INBOX_NOTEBOOK_GUID=YOUR_INBOX_NOTEBOOK_GUID
```

Установите `python` и далее используйте `pip`, чтобы установить все необходимые зависимости:
```
pip install -r requirements.txt
```

## Запуск проекта

К запуску доступны следующие скрипты:
1. list_notebooks.py - выводит в консоль guid и название всех журналов (notebooks), хранящихся в 'Evernote'. Для запуска скрипта используйте нижеследующую команду:
```
python list_notebooks.py
```
2. dump_inbox.py - выводит в консоль текста всех заметок (notes) из журнала inbox (переменная `INBOX_NOTEBOOK_GUID` файла `.env`). Также в качестве аргумента скрипт принимает количество записей для вывода. По умолчанию выводится 10 записей. Для запуска скрипта, с выводом 5 записей используйте нижеследующую команду:
```
python dump_inbox.py 5
```
3. add_note2journal.py - добавляет дату и день недели в журнал (переменная `JOURNAL_NOTEBOOK_GUID` файла `.env`) по шаблону из заметки (переменная `JOURNAL_TEMPLATE_NOTE_GUID` файла `.env`). В качестве аргумента можно передать собственную дату, либо будет использована текущая дата на момент вызова скрипта. Для запуска скрипта, с передачей собственной даты используйте нижеследующую команду:
```
python add_note2journal.py 2021-09-10
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
