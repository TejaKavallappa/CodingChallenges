public class CellRemoval{
	int[] parentCells;
	int del;
	int res=0;
	public int cellsLeft(int[] parent, int deletedCell){
		parentCells = parent;
		del = deletedCell;
		for(int i =0;i<parentCells.length;i++){
			if(parentCells[i]==-1 && del!=i)
				go(i);
		}
	}
	private void go(int now){
		boolean any = false;
		for(int i=0;i<parentCells.length;i++){
			if(parentCells[i]==now && i!=deleted){
				go(i);
				any = true;
			}
		}
		if(!any){
			res++;
		}
	}
}
