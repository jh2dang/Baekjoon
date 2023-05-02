import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
 
public class Main {
 
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
 
        int x = N; // x에 N을 저장.
        int cnt = 0; // 반복한 횟수.
        while (true) {
            int q = x / 10; // x의 십의 자리
            int r = x % 10; // x의 일의 자리
 
            int sum = q + r;
 
            x = r * 10 + sum % 10; // r과 sum의 가장 오른쪽 값을 더한다.
            cnt++;
 
            if (x == N) { // x와 N이 같아지는 순간 반복문을 종료.
                break;
            }
        }
 
        bw.write(cnt + "\n");
 
        bw.flush();
        bw.close();
        br.close();
    }
 
}
