import java.lang.Math;
import java.io.File;

public class DataGenerator {

    private static final String filepath = "dane.txt";

    public static void main(String[] args) {
        double numRecords = Math.random() * 50 + 20; 
        String[] records = new String[(int) numRecords];
        for (int i = 0; i < records.length; i++) {
            records[i] = generateRecord();
        }
        loadToFile(records);
    }

    private static void loadToFile(String[] records) {
        try {
            File file = new File(filepath);
            if (file.exists()) {
                file.delete();
            }
            java.io.FileWriter writer = new java.io.FileWriter(filepath, true);
            for (String record : records) {
                writer.write(record + "\n");
            }
            writer.close();
        } catch (Exception e) { 
            e.printStackTrace();
        }
    }

    private static String generateRecord() {
        long randomNumber = (long) (Math.random() * 1_000_000_000) + 1;
        String comment = Math.random() < 0.6 ? "//Sample comment." : "";
        boolean emptyLine = Math.random() < 0.1;
        String line;
        if (emptyLine) {
            line = comment;
        }else {
            line = randomNumber + " " + comment;
        }

        String prefix = Math.random() < 0.5 ? "\t" : " ";
        String suffix = Math.random() < 0.5 ? "\t" : " ";
        return prefix + line + suffix;
    }
}