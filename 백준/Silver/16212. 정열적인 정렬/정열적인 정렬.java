import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 수열의 길이 N 입력
        int N = sc.nextInt();

        // 수열 입력
        int[] sequence = new int[N];
        for (int i = 0; i < N; i++) {
            sequence[i] = sc.nextInt();
        }

        // 수열 정렬
        Arrays.sort(sequence);

        // 정렬된 수열 출력
        for (int i = 0; i < N; i++) {
            System.out.print(sequence[i] + " ");
        }
    }
}