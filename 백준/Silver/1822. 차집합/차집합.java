import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int a,b,i,t;
		HashMap<Integer,Boolean> map = new HashMap<>();
		StringTokenizer st = new StringTokenizer(br.readLine());
		a = Integer.parseInt(st.nextToken());
		b = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		for(i=0;i<a;i++) map.put(Integer.parseInt(st.nextToken()),true);
		st = new StringTokenizer(br.readLine());
		for(i=0;i<b;i++) {
			t = Integer.parseInt(st.nextToken());
			if(map.containsKey(t)) map.remove(t);
		}
        ArrayList<Integer> arr = new ArrayList<Integer>();
        for(int k:map.keySet()) arr.add(k);
        Collections.sort(arr);
        sb.append(arr.size()+"\n");
        if(arr.size()!=0) for(int k:arr) sb.append(k+" ");
        System.out.println(sb);
	}
}