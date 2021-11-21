package com.usatu.processor;
import joinery.DataFrame;
import java.io.*;
import java.util.Set;

// Реализация интерфейса DataProcessor для обработчика csv-файлов
public class CsvDataProcessor extends DataProcessor {

    private String separator = ";";     // разделитель столбцов csv-файла по умолчанию

    // Дополнительный setter для установки разделителя
    public void setSeparator(String sep) {
        this.separator = sep;
    }

    @Override
    public boolean read() {
        try {
            // Читаем файл данных
            File datasetFile = new File(this.datasource);
            InputStream dataStream = new FileInputStream(datasetFile);
            // Трансформируем в DataFrame с помощью встроенной функции readCsv
            dataset = DataFrame.readCsv(dataStream, separator);
            // Проверяем количество считанных из файла колонок
            Set<String> colNames = dataset.columns();
            // количество колонок < 2 возвращаем false
            if (colNames.size() < 2) return false;
            return true;
        } catch (IOException e) {
            System.out.println("Datasource error: " + e.getMessage());
            return false;
        }
    }

    @Override
    public void run() {
        result = sortByColName(dataset, "LKG", true);
    }

    @Override
    public void printResult() {
        System.out.println("CSV-file processor result:\n" + result);
    }

}

