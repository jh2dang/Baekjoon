import java.util.*;
public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int x = sc.nextInt();
		int y = sc.nextInt();
		int w = sc.nextInt();
		int h = sc.nextInt();
		
		System.out.println(Math.min(Math.min(Math.abs(y), Math.abs(y-h)), Math.min(Math.abs(x), Math.abs(x-w))));
	}
}