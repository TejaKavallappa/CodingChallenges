public class Egalitarianism{
//Not solved
	public static int maxDifference(String[] isFriend, int d){
		//Check length of isFriend array is same as array entry length
		//Convert to 2 D array
		int i =0, j, level=1;
		int size = isFriend.length;
		int[][] friends = new int[size][size];
		boolean levelChange = false;
		for (String s: isFriend){
			char[] sToChar = s.toCharArray();
			levelChange = false;
			for (j=0;j<sToChar.length-1;j++){
				char c = sToChar[j];
				if (c=='Y'){
					friends[i][j]=-1;
				}
			}

			i++;
		}
		for(i=0;i<friends.length;i++){
			levelChange = false;
			for(j=0;j<friends.length;j++){
				if (friends[i][j]==-1){
					friends[i][j]=level;
					friends[j][i]=level;
					levelChange = true;
				}
			}
			if (levelChange) level++;
		}
	for( i =0;i<friends.length;i++){
			for ( j =0;j<friends.length;j++){
				System.out.print(friends[i][j] + " ");
			}
			System.out.println();
		}


			if (level==1)
			return -1;
		return (level-2)*d;		
	}
	public static void main(String[] args)
	{
		String[] isFriend ={"NNYNNN", "NNYNNN", "YYNYNN", "NNYNYY",
			 "NNNYNN", "NNNYNN"};
		int maxD = maxDifference(isFriend,1000);
		System.out.println("Maximum Difference is "+maxD);
	}
}
