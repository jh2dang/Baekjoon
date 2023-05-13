import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

interface Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        String[] input = br.readLine().split(" ");
        int a = Integer.parseInt(input[0]), b = Integer.parseInt(input[1]), c = Integer.parseInt(input[2]), d = Integer.parseInt(input[3]), e = Integer.parseInt(input[4]), f = Integer.parseInt(input[5]);

        for(int x = -999; x<1000; x++) {
            for(int y = -999; y<1000; y++) {
                if(a * x + b * y == c && d * x + e * y == f) {
                    System.out.println(x + " " + y);
                    break;
                }
            }
        }
    }
}