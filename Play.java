import java.io.*;

public class Play {

    public void show(long y) throws Exception {
        String fileName = "txt\\" + y + ".txt";
        File f = new File(fileName);
        char[] ch = new char[1950];
        Reader read = new FileReader(f);
        int count = read.read(ch);
        read.close();
        System.out.println(new String(ch, 0, count));
    }

    public static void main(String[] args) throws Exception {
        Play play = new Play();
        long start = System.nanoTime() / 1000;
        do {
            long use = System.nanoTime() / 1000 - start;
            play.show(use / 50000 + 1);
            if (use >= 219000050) {
                break;
            }
        } while (true);

    }
}