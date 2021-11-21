from abc import ABC, abstractmethod     # подключаем инструменты для создания абстрактных классов
import pandas   # библиотека для работы с датасетами
import os

"""
    В данном модуле реализуются классы обработчиков для 
    применения алгоритма обработки к различным типам файлов (csv или txt).
    
    ВАЖНО! Если реализация различных обработчиков занимает большое 
    количество строк, то необходимо оформлять каждый класс в отдельном файле
"""

# Родительский класс для обработчиков файлов
class DataProcessor(ABC):
    def __init__(self, datasource):
        # общие атрибуты для классов обработчиков данных
        self._datasource = datasource   # путь к источнику данных
        self._dataset = None            # входной набор данных
        self.result = None              # выходной набор данных (результат обработки)
        self._max_value = None          # максимальное значение
        self._min_value = None          # минимальное значение
        self._average_value = None      # среднее значение

    # Метод, инициализирующий источник данных
    # Все методы, помеченные декоратором @abstractmethod, ОБЯЗАТЕЛЬНЫ для переопределения
    @abstractmethod
    def read(self) -> bool:
        pass

    # Точка запуска методов обработки данных
    @abstractmethod
    def run(self):
        pass

    """
        Пример одного из общих методов обработки данных.
        В данном случае метод просто сортирует входной датасет по значению заданной колонки (аргумент col)
        
        ВАЖНО! Следует логически разделять методы обработки, например, отдельный метод для сортировки, 
        отдельный метод для удаления "пустот" в датасете и т.д. Это позволит гибко применять необходимые
        методы при переопределении метода run для того или иного типа обработчика.
        НАПРИМЕР, если ваш источник данных это не файл, а база данных, тогда метод сортировки будет не нужен,
        т.к. сортировку можно сделать при выполнении SQL-запроса типа SELECT ... ORDER BY...
    """
    def sort_data_by_col(self, df, colname, asc) -> pandas.DataFrame:
            return df.sort_values(by=[colname], ascending=asc)

    # Абстрактный метод для вывод результата на экран
    @abstractmethod
    def print_result(self):
        pass

    # Абстрактный метод для поиска аномальных значений (максимум и минимум за весь период)
    @abstractmethod
    def search_abnormal_value(self):
        pass

    # Абстрактный метод для поиска среднего значение за весь период
    def search_average_value(self):
        pass

    # Абстрактный метод для выявления статистики за определенный период
    @abstractmethod
    def stat_for_period(self):
        pass

# Реализация класса-обработчика csv-файлов
class CsvDataProcessor(DataProcessor):
    # Переопределяем конструктор родительского класса
    def __init__(self, datasource):
        # инициализируем конструктор родительского класса для получения общих атрибутов
        DataProcessor.__init__(self, datasource)
        self.separator = ';'        # дополнительный атрибут - сепаратор по умолчанию
    """
        Переопределяем метод инициализации источника данных.
        Т.к. данный класс предназначен для чтения CSV-файлов, то используем метод read_csv
        из библиотеки pandas
    """
    def read(self):
        try:
            self._dataset = pandas.read_csv(self._datasource, sep=self.separator, header='infer', names=None, encoding="utf-8")
            # Читаем имена колонок из файла данных
            col_names = self._dataset.columns
            # Если количество считанных колонок < 2 возвращаем false
            if len(col_names) < 2:
                return False
            return True
        except Exception as e:
            print(str(e))
            return False

    # Сортируем данные по значениям введенной колонки и сохраняем результат в атрибуте result
    def run(self):
        sort_by = input('Введите столбец по которому нужно сортировать: ')
        self.result = self.sort_data_by_col(self._dataset, sort_by, True)

    # Поиск аномальных значений (максимум и минимум за весь период)
    def search_abnormal_value(self):
        self._max_value = self.result.max()
        self._min_value = self.result.min()

    # Среднее значение за весь период
    def search_average_value(self):
        self._average_value = self.result.mean()

    # Статистика за определенный период (вводим диапазон с клавиатуры)
    def stat_for_period(self):
        date_start = input('Введите начальную дату (гггг-мм-дд чч): ') + ':00:00'
        date_end = input('Введите конечную дату (гггг-мм-дд чч): ') + ':00:00'
        result = self._dataset.loc[(self._dataset['datetime'] >= date_start) & (self._dataset['datetime'] <= date_end)]
        print(result)

    # Вывод результатов работы
    def print_result(self):
        print('Таблица из датасета (изначальная): ', self._datasource, '\n', self._dataset)
        print('Таблица из датасета (отсортированная): ', '\n', self.result)
        self.search_abnormal_value()
        print('Максимальное значение: \n', self._max_value, '\n', 'Минимальное значение: \n', self._min_value)
        self.search_average_value()
        print('Среднее значение: \n', self._average_value)


"""
# Реализация класса-обработчика txt-файлов
class TxtDataProcessor(DataProcessor):
    # Реализация метода для чтения TXT-файла
    def read(self):
        try:
            self._dataset = pandas.read_table(self._datasource, sep='\s+', engine='python')
            col_names = self._dataset.columns
            if len(col_names) < 2:
                return False
            return True
        except Exception as e:
            print(str(e))
            return False

    def run(self):
        self.result = self.sort_data_by_col(self._dataset, "LKG", True)

    def print_result(self):
        print(f'Running TXT-file processor!\n', self.result)
"""