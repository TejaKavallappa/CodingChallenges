import java.io.*;
import java.util.Scanner;
import java.lang.StringBuilder;
public class RemoveCharacters{ 
    public static void main(String[] args){
        try{
            Scanner readfile = new Scanner(new File("test_removecharacters.txt"));
            String test;
            while(readfile.hasNext()){
                test = readfile.nextLine().trim();
                System.out.println(test);
                String[] parts = test.split(",");
                String sent = parts[0];
                String rem = parts[1].trim();
                StringBuilder res = new StringBuilder();
                for(int i = 0; i < sent.length(); i++){
                    char c = sent.charAt(i);
                    boolean match = false;
                    for (int j = 0; j < rem.length(); j++){
                        if (c == rem.charAt(j)){
                            match = true;
                            break;
                        }
                    }
                    if (!match)
                        res = res.append(c);
                }                
                System.out.println(res.toString());
            }
        }
        catch(FileNotFoundException e){
            System.out.println("File not found");
        }    
    }
}
