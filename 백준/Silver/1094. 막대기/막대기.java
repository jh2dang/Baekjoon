import java.util.*;
import java.io.*;

public class Main {
    public static void main (String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int min = 64;
        int cur = min;
        int X = Integer.parseInt(br.readLine());
        int result = 1;
        while (cur != X) {
            min = min / 2;
            if (X <= cur - min) {
                cur -= min;
                result--;
            }
            result++;
        }
        bw.write(String.valueOf(result));
        bw.flush();
    }
}