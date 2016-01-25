/*Approach: Due to the very large size of the test file, this program doesn't work. However, for smaller triangles this program generates the correct answer.
 * My approach: for each new row read in, add each value to the previous two sums.
 * The sum values of each row are stored in a queue. 
 * Solution that works: Dynamic Programming (Yet to learn)
 */
import java.util.Queue;
import java.util.LinkedList;
import java.util.Scanner;
import java.io.*;
public class TriangleSum{ 
    public static void main(String[] args){
        long starttime = System.currentTimeMillis();
        Queue<Integer> prevsumQueue = new LinkedList<Integer>();
        try{
            Scanner rfile = new Scanner(new File("smalltriangle.txt"));
            //Scanner rfile = new Scanner(new File("triangle.txt"));
            String test;
            int sum1 = 0, qLen, max = Integer.MIN_VALUE, i = 0,j = 0;
            //int linenum = 0;
            while(rfile.hasNext()){
                //linenum++;
                //System.out.println(linenum);
                test = rfile.nextLine();
                test = test.trim();
                String[] numstr = test.split(" ");
                int nums[] = new int[numstr.length];
                //Read in the numbers in each line into a queue
                i = 0;
                for(String strNum:numstr){
                    nums[i++] = Integer.parseInt(strNum);
                }
                //First line of triangle. 
                if (numstr.length == 1){
                    prevsumQueue.add(Integer.parseInt(numstr[0]));
                    continue;
                }
                qLen = prevsumQueue.size();
                j = 0;
                while(qLen > 0){
                    qLen--;
                    sum1 = prevsumQueue.poll();
                    int num1 = 0, num2 = 0; 
                    if(j < nums.length){
                        num1 = nums[j];
                    }
                    if(j+1 < nums.length){
                        num2 = nums[j+1];
                    }
                    j++;
                    
                    prevsumQueue.add(sum1 + num1);
                    prevsumQueue.add(sum1 + num2);
                }
                //System.out.println();
            }
            for(int i: prevsumQueue){
                if(i > max){
                    max = i ;
                }
            }
            System.out.println(max);
            long endtime = System.currentTimeMillis();
            System.out.println("Took "+ (endtime - starttime) + "ms");

        }
        catch(IOException e){
            System.out.println("Cannot find file.");
        }
    }

}
