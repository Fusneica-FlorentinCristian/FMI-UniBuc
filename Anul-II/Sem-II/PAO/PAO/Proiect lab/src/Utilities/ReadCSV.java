package Utilities;

import Services.EventService;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class ReadCSV {

    private BufferedReader csvReader;

    private static ReadCSV instance = null;

    private ReadCSV() {

    }

    public static ReadCSV getInstance() {
        if(instance == null) {
            instance = new ReadCSV();
        }
        return instance;
    }

    public void readFile(String path) throws IOException {
        csvReader = new BufferedReader(new FileReader(path));
        String row;
        while ((row = csvReader.readLine()) != null) {
            String[] data = row.split(",");
            // do something with the data
            System.out.println(data[0]);
        }
        csvReader.close();
    }
}
