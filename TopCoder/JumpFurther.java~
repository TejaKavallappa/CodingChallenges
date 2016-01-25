public class JumpFurther{
	public static int furthest(int N, int badStep){
		int thisStep = 0;
		for(int i =1;i<=N;i++){
			if((thisStep+i)==badStep) continue;
			thisStep += i;
		}
		return thisStep;
	}
	public static void main(String[] args){
		int N, badStep;
		if (args.length != 2){
			N = 2;
			badStep = 2;
		}
		else {
			N = Integer.parseInt(args[0]);
			badStep = Integer.parseInt(args[1]);
		}
		System.out.println("Final step = "+furthest(N,badStep));
	}

}
