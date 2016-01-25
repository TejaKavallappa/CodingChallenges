//Solved
import java.util.*;
public class SurveillanceSystem{
	public static String getContainerinfo(String containers,int[] reports,int L){
		int numSectors = containers.length();
		int numCams = reports.length;
		char[] result = new char[numSectors];
		Arrays.fill(result,'-');
		System.out.println(new String(result));
		// Identify sector subsections of size L
		// For each subString see if it matches report[j];
		int pos = 0;
		for(int j:reports){
			HashMap<Integer,Integer> monitoredSectors = new HashMap<Integer,Integer>();
			int count =0;
			for(int i =0;i<=numSectors-L;i++){
				String bunchSectors = containers.substring(i,i+L);
				int containersInL = numMatches(bunchSectors);
				if(j==containersInL){
					count++;
					for(int p = i;p<i+L;p++){
						if(monitoredSectors.get(p)==null)
							monitoredSectors.put(p,1);
						else
							monitoredSectors.put(p,(Integer) monitoredSectors.get(p)+1);
					}
				}
				if (count == 1){
					for(Integer it:monitoredSectors.keySet())
						result[it]='+';
				}
				else if (count>1){
					for(Integer that:monitoredSectors.keySet()){
						if (monitoredSectors.get(that)==count)
							result[that]='+';
						else result[that] = '?';
					}
				}

			}
			pos++;
		}
		return new String(result);
	}
	private static int numMatches(String string){
		int numContainers =0;
		for(int i =0;i<string.length();i++){
			if (string.charAt(i)=='X')
				numContainers++;
		}
		return numContainers;
	}
	public static void main(String[] args){
		String containers = new String("-XXXXX-");
		int[] reports = {2};

		int L = 3;
		String result = getContainerinfo(containers,reports,L);
		System.out.println(result);
	}

}

