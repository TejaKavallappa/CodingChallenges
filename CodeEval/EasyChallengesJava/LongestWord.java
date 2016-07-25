/*
 * Find the longest word in a sentence. If multiple words of longest length
 * exist, pick the first one
 */
import java.io.*;
public class LongestWord{ 
    public static void main(String[] args) throws IOException{
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while((line = buffer.readLine()) != null){
            line = line.trim();
            int maxLength = 0;
            String maxString = "";
            for (String word : line.split(" ")){
                if (word.length() > maxLength){
                    maxLength = word.length();
                    maxString = word;
                }
            }
            System.out.println(maxString);
        }
    }
}
