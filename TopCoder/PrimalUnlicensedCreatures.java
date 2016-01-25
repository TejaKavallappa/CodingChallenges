public class PrimalUnlicensedCreatures{

	public static int maxWins(int initiallevel, int[] grezPower){
		int maxWins=0, score = initiallevel;
		boolean eat=false;
		while(true){
			eat = false;
			for(int i =0;i<grezPower.length; i++){
				if(grezPower[i]<score){
					score += grezPower[i]/2;
					grezPower[i]=Integer.MAX_VALUE;
					eat = true;
					maxWins++;
				}
			}
			if (eat==false)
				break;
		}
		return maxWins;
	}
	public static void main(String[] args){
		int[] grezPower ={3,13,6,4,9};
		int initiallevel = 3;
		System.out.println(maxWins(initiallevel,grezPower));
	}
}
