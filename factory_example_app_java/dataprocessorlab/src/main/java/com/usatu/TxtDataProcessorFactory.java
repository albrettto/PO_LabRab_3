package com.usatu;
import com.usatu.processor.DataProcessor;
import com.usatu.processor.TxtDataProcessor;

/*
    Фабрика класса TxtDataProcessor создает экземпляр класс и инициализирует источник данных.
    Если инициализация прошла успешно, возвращаем экземпляр, если нет - null
*/

public class TxtDataProcessorFactory extends DataProcessorFactory {

    @Override
    public DataProcessor getProcessor(String source) {
        TxtDataProcessor instance = new TxtDataProcessor();
        instance.setDatasource(source);
        if (instance.read()) {
            return instance;
        }
        else {
            return null;
        }
    }
}
