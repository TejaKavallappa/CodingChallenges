import java.util.*;
public class DeerInZooDivTwo{
	public static int[] getminmax(int argN, int argK){
		int[] result = new int[2];
		int min = (argN-argK);
		int max = (2*argN - argK)/2;
		if (min < 0){
			min = 0;
		}
		result[0] = min; 		
		result[1] = max;
		return result;
	}
	public static void main(String[] args){
		int N=3, K=2;
		if (args.length == 2){
			N = Integer.parseInt(args[0]);
			K = Integer.parseInt(args[1]);
		}
		int[] result = getminmax(N,K);
		for(int a:result)
			System.out.println(a+" ");
	}
}
