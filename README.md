# Парсер документации Python
Приложение для получения информации о нововведениях python, статусов версий Python,
скачивание архива документации Python? а также подсчета количества PEP с сайта "https://peps.python.org/"
в каждом статусе и общее количество PEP

## Установка
1. Клонирование репозитория
git clone https://github.com/LextNet/bs4_parser_pep.git
cd bs4_parser_pep
2. Настройка переменных окружения и установка необходимых библиотек
pip install -r requirements.txt

## Запуск
Парсер документации Python

positional arguments:
  {whats-new,latest-versions,download,pep}
                        Режимы работы парсера

options:
  -h, --help            show this help message and exit
  -c, --clear-cache     Очистка кеша
  -o {pretty,file}, --output {pretty,file}  (Дополнительные способы вывода данных)

# Запуск парсера информации из статей о нововведениях в Python.
(venv) ...$ python main.py whats-new

# Запуск парсера статусов версий Python.
(venv) ...$ python main.py latest-versions

# Запуск парсера, который скачивает архив документации Python.
(venv) ...$ python main.py download

# Запуск парсера, который формирует csv файл для подсчета статусов PEP.
(venv) ...$ python main.py pep