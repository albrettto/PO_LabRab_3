package com.usatu;
import com.usatu.processor.*;

/*
    Пример запуска обработчика данных и вывода результата обработки с помощью фабрики.

    ВАЖНО! Обратите внимание, что функция принимает в качестве аргумента базовый абстрактный класс DataProcessor
    и будет выполняться для любого типа обработчика данных (CSV или TXT), что позволяет в дальнейшем расширять
    приложение, просто добавляя другие классы обработчиков, которые, например, работают с базой данных или FTP-сервером.
    Основное условие для расширения - это сохранение формата выходных данных
    (в данном примере результатом обработки является тип joinery.DataFrame)
*/

public class AppMain {

    public static void main(String[] args) {
        DataProcessor proc = initProcessor("C:\\Users\\Bogdan\\Desktop\\УГАТУ\\Проектирование и конструирование ПО\\factory_example_app_java\\seeds_dataset.csv");
        if (proc != null) runProcessor(proc);
    }

    // Инициализация обработчика
    // В зависимости от расширения файла вызываем соответствующий фабричный метод
    public static DataProcessor initProcessor(String source) {
        DataProcessorFactory procFactory;
        if (source.endsWith(".csv")) {
            procFactory = new CsvDataProcessorFactory();
            return procFactory.getProcessor(source);
        }
        else if (source.endsWith(".txt")) {
            procFactory = new TxtDataProcessorFactory();
            return procFactory.getProcessor(source);
        }
        return null;
    }

    // Запуск обработки
    public static void runProcessor(DataProcessor proc) {
        proc.run();
        proc.printResult();
    }

}
