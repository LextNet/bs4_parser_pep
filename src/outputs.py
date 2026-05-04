import csv
import datetime as dt
import logging

from prettytable import PrettyTable

from constants import (
    BASE_DIR, DATETIME_FORMAT, MAX_STATUS_LENGTH, MAX_COUNT_LENGTH,
    TOTAL_WIDTH, OUTPUT_PRETTY_TABLE, OUTPUT_FILE, RESULTS_DIR
)


def control_output(results, cli_args):
    output = cli_args.output
    if output == OUTPUT_PRETTY_TABLE:
        # Вывод данных в PrettyTable.
        pretty_output(results)
    elif output == OUTPUT_FILE:
        # Вывод данных в файл csv.
        file_output(results, cli_args)
    else:
        # Вывод данных по умолчанию — в терминал построчно.
        default_output(results)


def default_output(results):
    # Печатаем список results построчно.
    for row in results:
        print(*row)


def pretty_output(results):
    table = PrettyTable()
    # В качестве заголовков устанавливаем первый элемент списка.
    table.field_names = results[0]
    # Выравниваем всю таблицу по левому краю.
    table.align = 'l'
    # Добавляем все строки, начиная со второй (с индексом 1).
    table.add_rows(results[1:])
    # Печатаем таблицу.
    print(table)


def write_pep_format(file_path, results):
    with open(file_path, 'w', encoding='utf-8') as f:
        for row in results:
            status, count = row
            currow = (
                f"| {status:<{MAX_STATUS_LENGTH}}| {count:>{MAX_COUNT_LENGTH}}"
                f"|\n"
            )
            f.write('=' * TOTAL_WIDTH + '\n')
            f.write(currow)
        # Нижняя граница таблицы
        f.write('=' * TOTAL_WIDTH + '\n')


def write_default_format(file_path, results):
    with open(file_path, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, dialect='unix')
        writer.writerows(results)


def file_output(results, cli_args):
    results_dir = BASE_DIR / RESULTS_DIR
    results_dir.mkdir(exist_ok=True)
    # Получаем режим работы парсера из аргументов командной строки.
    parser_mode = cli_args.mode
    now = dt.datetime.now()
    now_formatted = now.strftime(DATETIME_FORMAT)
    # «режим работы программы» + «дата и время записи» + формат (.csv).
    file_name = f'{parser_mode}_{now_formatted}.csv'
    # Получаем абсолютный путь к файлу с результатами.
    file_path = results_dir / file_name
    # для режима PEP выводим в табличном виде:
    if parser_mode == 'pep':
        write_pep_format(file_path, results)
    else:
        # Передаём в метод writerows список с результатами парсинга.
        write_default_format(file_path, results)
    logging.info(f'Файл с результатами был сохранён: {file_path}')
