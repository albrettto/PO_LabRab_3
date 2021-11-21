package com.usatu.processor;
import com.sun.jdi.Value;
import joinery.DataFrame;

/*
    Общий интерфейс обработчиков данных

    В классической реализации Factory Pattern классы должны иметь общий интерфейс (interface),
    но, т.к. обработчики данных , очевидно, будут иметь ряд общих методов и атрибутов (reusable code),
    то необходимо применение абстрактного класса.
 */

public abstract class DataProcessor {
    protected String datasource;  // путь для подключения к источнику данных
    protected DataFrame dataset;  // входной датасет, который инициализируется методом read()
    protected DataFrame result;   // выходной датасет (результат обработки)

    // Setter для установки пути подключения к источнику данных
    public void setDatasource(String source) {
        this.datasource = source;
    }
    // Getter для получения результата (выходного DataFrame)
    public DataFrame getGetresult() {
        return this.result;
    }

    // Чтение источника данных
    public abstract boolean read();
    // Запуск обработки данных
    public abstract void run();
    // Вывод результатов обработки данных
    public abstract void printResult();

    /*
        ВАЖНО! В базовом абстрактном классе также нужно разместить
        общие методы для обработки данных, т.е. те методы, которые
        будут использоваться в наследниках при запуске метода run()

        Пример одного из общих методов обработки данных.
        В данном случае метод просто сортирует входной датасет по значению заданной колонки (аргумент col)
    */

    protected DataFrame sortByColName(DataFrame df, String colName, boolean asc) {
        // если asc == true сортируем по возрастанию, иначе по убыванию
        if (asc) return df.sortBy(colName);
        else return df.sortBy("-" + colName);
    }

    /*
        ВАЖНО! Следует логически разделять методы обработки, например, отдельный метод для сортировки,
        отдельный метод для удаления "пустот" в датасете и т.д. Это позволит гибко применять необходимые
        методы при переопределении метода run() для того или иного типа обработчика.
        НАПРИМЕР, если ваш источник данных это не файл, а база данных, тогда метод сортировки будет не нужен,
        т.к. сортировку можно сделать при выполнении SQL-запроса типа SELECT ... ORDER BY...
    */
}

