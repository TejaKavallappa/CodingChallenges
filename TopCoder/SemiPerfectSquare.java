public class SemiPerfectSquare{
	public static String check(int N){
		if (N<=1) return new String("No");
		for(int i =2;i<=N/2;i++){
			if (N%(i*i)==0){
				int semi = N/(i*i);
				if (semi*i*i == N && semi<i)
					return new String("Yes");
			}
		
		}
		return new String("No");
	}
	public static void main(String[] args){
		int N = 4;
		if(args.length != 0){
			N = Integer.parseInt(args[0]);
		}
		System.out.println(check(N));
	}
}
