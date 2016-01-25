import java.io.*;
import java.util.*;

public class SumOfIntegers{ 
    public static void main(String[] args){
        try{
        Scanner readfile = new Scanner(new File("test_sumofints.txt"));
        String line;
        int maxEnding = 0, maxSlice = 0, maxVal = Integer.MIN_VALUE;
        while(readfile.hasNext()){
            line = readfile.next();
            String[] numstr = line.split(",");
            int numArr[] = new int[numstr.length];
            for (int i = 0; i < numstr.length; i++){
                numArr[i] = Integer.parseInt(numstr[i]);
                maxEnding = Math.max(0, maxEnding + numArr[i]);
                maxSlice = Math.max(maxSlice, maxEnding);
                maxVal = Math.max(maxVal, numArr[i]);
            }
            if (maxSlice == 0){
                System.out.println(maxVal);
            }
            else {
                System.out.println(maxSlice);
            }
        }   
        }
        catch(FileNotFoundException e){
            
        }     
    }
}
