import os
from processor.dataprocessorfactory import *

"""
    Пример простейшей функции, которая запускает обработчик данных и выводит результат обработки (возвращает None).
    
    ВАЖНО! Обратите внимание, что функция принимает в качестве аргумента базовый абстрактный класс DataProcessor
    и будет выполняться для любого типа обработчика данных (CSV или TXT), что позволяет в дальнейшем расширять
    приложение, просто добавляя другие классы обработчиков, которые, например, работают с базой данных или FTP-сервером.
    Основное условие для расширения - это сохранение формата выходных данных 
    (в данном примере результатом обработки является тип pandas.DataFrame)
"""

# В зависимости от расширения файла вызываем соответствующий фабричный метод
def init_processor(source: str) -> DataProcessor:
    proc = None
    if source.endswith('.csv'):
        proc = CsvDataProcessorFactory().get_processor(source)
    '''elif source.endswith('.txt'):
        proc = TxtDataProcessorFactory().get_processor(source)'''
    return proc

# Запуск обработки
def run_processor(proc: DataProcessor) -> None:
    proc.run()
    proc.print_result()

if __name__ == '__main__':
    proc = init_processor("temperature.csv")
    if proc is not None:
        run_processor(proc)
    proc = init_processor("humidity.csv")
    if proc is not None:
        run_processor(proc)
    proc = init_processor("pressure.csv")
    if proc is not None:
        run_processor(proc)
    proc = init_processor("wind_direction.csv")
    if proc is not None:
        run_processor(proc)
    proc = init_processor("wind_speed.csv")
    if proc is not None:
        run_processor(proc)

date_start = input('Введите начальную дату (гггг-мм-дд чч)') + ':00:00'
date_end = input('Введите конечную дату (гггг-мм-дд чч)') + ':00:00'
proc.stat_for_period(date_start, date_end)