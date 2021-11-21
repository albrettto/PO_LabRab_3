package com.usatu;
import com.usatu.processor.*;

/*
    Фабричный метод может не только возвращать класс соответствующего обработчика,
    здесь также может быть реализована логика, которая меняет поведение данного обработчика,
    например, меняет тип разделителя и кодировку для CSV-файла (через атрибуты класса),
    применяет различные режимы обработки и т.д. (см. CsvDataProcessorFactory)
*/

public abstract class DataProcessorFactory {
    public abstract DataProcessor getProcessor(String source);
}
