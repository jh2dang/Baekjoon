import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        
        int yuk = 666;
        int cnt = 0;

        while (cnt < N) {
            if (String.valueOf(yuk).contains("666")) {
                cnt++;
            }
            yuk += 1;
        }

        System.out.println(yuk - 1);
    }
}