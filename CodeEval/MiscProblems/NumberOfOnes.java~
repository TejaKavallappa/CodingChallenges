import java.io.*;
import java.util.Scanner;
public class NumberOfOnes{
    public static void main(String[] args){
        try{
            Scanner readfile = new Scanner(new File("test_numberofones.txt"));
            String line;
            while(readfile.hasNext()){
                line = readfile.nextLine().trim();
                int num = Integer.parseInt(line);
                int res;
                System.out.println(num );
                num = num - ((num >>> 1) & 0x55555555);
                num = (num & 0x33333333) + ((num >>> 2) & 0x33333333);
                num = (num + (num >>> 4)) & 0x0f0f0f0f;
                num = num + (num >>> 8);
                num = num + (num >>> 16);
                res = num & 0x3f;
                System.out.println(res);
                System.out.println("---------------------");

            }
        }
        catch(FileNotFoundException e){
            System.out.println("File not found.");
        }

    }

}
