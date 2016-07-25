/* Input file will contain a comma separated list of sorted numbers and then the sum 'X', separated by semicolon
 */
import java.util.*;
import java.io.*;
public class SumToX{ 
    public static int binSearch(int rem, int[] numarray){
        int mid; 
        int low = 0, high = numarray.length-1;
        while(low <= high ){
            mid = low + (high-low)/2;
            if (numarray[mid] == rem)
                return mid;
            if (numarray[mid] < rem)
                low = mid+1;
            if (numarray[mid] > rem)
                high = mid-1;
        }    
        return -1;
    }

    public static void main(String[] args) throws IOException{
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while((line = buffer.readLine()) != null){
            line = line.trim();
            System.out.println(line);
            int target = Integer.parseInt(line.split(";")[1]);
            String[] nums = line.split(";")[0].split(",");
            int[] inums = new int[nums.length];
            for(int i = 0; i < inums.length; i++)
                inums[i] = Integer.parseInt(nums[i]);
            ArrayList<Integer> minRes = new ArrayList<Integer>();
            for(int i = 0; i < inums.length; i++){
                //System.out.println("Considering "+inums[i]+ " "+(target-inums[i]));
                int num1 = inums[i];
                int rem = target - num1;
                //Search for rem in array
                int posrem = binSearch(rem,inums);
                if (posrem != -1 && i != posrem){
                    //int n1 = Math.min(num1,rem);
                    int n1 = Math.min(i,posrem);
                    if (!minRes.contains(n1)){
                        if(!minRes.isEmpty())
                            System.out.print(";");
                        minRes.add(n1);
                        System.out.print(num1 + ","+ inums[posrem]); 
                    }
                }
            }
            if (minRes.isEmpty())
                System.out.println("NULL");
            else
                System.out.println();
        }
    
    }

}
