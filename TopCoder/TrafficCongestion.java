public class TrafficCongestion{
	private int minCars;
	boolean[] visitedCities; 

	public int theMinCars(int treeHeight){
		int numCities = (int) Math.pow(2,treeHeight+1)-1;
		visitedCities = new boolean[numCities+1];
		for(boolean city: visitedCities){
			city = false;
		}
		tryPaths(numCities);
		return minCars;
	}

	private void tryPaths(int numCities){
		for (int i = numCities; i>1 ; i--){
			if (visitedCities[i]==false){
				minCars++;
				visitedCities[i]=true;
				pathExists(i, numCities);
			}
		}
		return;
	}
	private void pathExists(int visitingCity, int numCities){
		if (visitingCity/2 > 0 && visitedCities[visitingCity/2]==false) {
			visitedCities[visitingCity/2] = true;
			pathExists(visitingCity/2, numCities);
		}
		else if (visitingCity*2 < (numCities+1) && visitedCities[visitingCity*2]==false){
			visitedCities[visitingCity*2] = true;
			pathExists(visitingCity*2, numCities);
		}
		return;	
	}
}
