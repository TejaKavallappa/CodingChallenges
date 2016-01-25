import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class ColumnName{ 
    public static void main(String[] args){
        //Read path to file name from stdin
        Scanner scanner = new Scanner(System.in);
        String fileName = scanner.nextLine();
        //Using try read the file
        try{
            Scanner readFile = new Scanner(new File(fileName));
            int colNum,a;
            String letters = new String("ABCDEFGHIJKLMNOPQRSTUVWXYZ");

            while(readFile.hasNext()){
                StringBuffer res = new StringBuffer();
                colNum = readFile.nextInt();
                while(colNum > 0){
                    a = (colNum-1)%26;
                    res.append(letters.charAt(a));
                    colNum = (colNum-a)/26;
                }
                System.out.println(res.reverse().toString());
            }//while
        }//try
        catch(FileNotFoundException e){
            System.out.println("File Not found");
        }
    }//main
}//ColumnName
