public class InsertZ{
	
	public static String canTransform(String init, String goal){
		if ((init==null) || (goal==null))
			throw new IllegalArgumentException("Enter valid string");
		if (init.length()>goal.length())
			return new String("No");
		//Make sure init and goal chars are lower case
		init.toLowerCase();
		goal.toLowerCase();
		int initPtr = 0, goalPtr = 0;
		while(initPtr<init.length() || goalPtr<goal.length()){
			if((initPtr<init.length()) && init.charAt(initPtr) == goal.charAt(goalPtr)){
				initPtr++; goalPtr++;
			}
			else if (goal.charAt(goalPtr) == 'z'){
				goalPtr++;
			}
			else return new String("No");
		}


		return new String("Yes");
	}
	public static void main(String[] args){
		String init,goal;
		if (args.length == 0)
		{
			init = new String("fox");
			goal = new String("fozx");
		}
		init = args[0];
		goal = args[1];
		System.out.println(canTransform(init,goal));
	}
}
