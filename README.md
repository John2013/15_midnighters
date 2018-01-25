# Night Owls Detector

Определение пользователей, отправивших задачи на
[DEVMAN.org](https://devman.org) ночью.

# Как установить

Python 3 должен быть установлен.

```bash
$ pip install -r requirements.txt  # или pip3
```

Рекомендуется использовать [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/).

# Как запустить

```
usage: seek_dev_nighters.py [-h] [--pages_count PAGES_COUNT]

Получить список сов девмана.

optional arguments:
  -h, --help            show this help message and exit
  --pages_count PAGES_COUNT, -p PAGES_COUNT
                        Количество страниц (по умолчанию 10)
```

Пример:
```bash
python seek_dev_nighters.py # или python3
```

Ответ:
```
Полуночники девмана:
Петя
Вася
Света
```


# Задачи проекта

Код написан в целях обучения.
Тренировочные курсы для web-разработчиков -
[DEVMAN.org](https://devman.org)
