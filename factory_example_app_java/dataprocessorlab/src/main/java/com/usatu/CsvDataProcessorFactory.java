package com.usatu;
import com.usatu.processor.DataProcessor;
import com.usatu.processor.CsvDataProcessor;

/*
    Фабрика класса CsvDataProcessor создает экземпляр класс и инициализирует источник данных.
    Если инициализация прошла успешно возвращаем экземпляр, иначе пробуем другие типы разделителей для csv,
    если все попытки неуспешны, возвращаем - null
*/

public class CsvDataProcessorFactory extends DataProcessorFactory {
    CsvDataProcessor instance;

    @Override
    public DataProcessor getProcessor(String source) {
        instance = new CsvDataProcessor();
        instance.setDatasource(source);
        if (instance.read()) {
            return instance;
        }
        else if (readWithSeparator(",")) {
            return instance;
        }
        else {
            return null;
        }
    }

    // метод для чтения csv-файла с другими типами сепараторов
    public boolean readWithSeparator(String sep) {
        instance.setSeparator(sep);
        if (instance.read()) {
            return true;
        }
        else {
            return false;
        }
    }
}
