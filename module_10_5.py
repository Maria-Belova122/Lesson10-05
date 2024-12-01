# ЗАДАНИЕ ПО ТЕМЕ "Многопроцессорное программирование"

import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []  # Список для считываемых строк
    # Открываем файл на чтение
    with open(name, 'r', encoding='utf-8') as current_file:
        # Запускаем бесконечный цикл
        while True:
            # Считываем файл построчно
            line = current_file.readline()
            if line:  # Считанная строка не пустая
                all_data.append(line)  # Добавляем строку в список
            else:  # Считанная строка пустая
                break  # Останавливаем цикл


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
# start_time1 = datetime.now()
# for file in filenames:
#     read_info(file)
# finish_time1 = datetime.now()
# function_time1 = finish_time1 - start_time1
# print('Время выполнения при линейном вызове -', function_time1)

# Многопроцессорный вызов
if __name__ == '__main__':
    start_time2 = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    finish_time2 = datetime.now()
    function_time2 = finish_time2 - start_time2
    print('Время выполнения при многопроцессорном вызове -', function_time2)
