/*
 * Input: stop football play
 * Output: f *o **o ***t ****b *****a ******l *******l
 */
import java.io.*;
public class StepwiseWord{ 
    public static void main(String[] args) throws IOException{
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while((line = buffer.readLine()) != null){
            line = line.trim();
            int maxLen = 0;
            String maxWord = "";
            for (String word: line.split(" ")){
                if (word.length() > maxLen){
                    maxWord = word;
                    maxLen = word.length();
                }
            }
            StringBuffer sb = new StringBuffer();
            int i = 1;
            for(char c: maxWord.toCharArray()){
                for(int j = 1; j < i; j++)
                    sb.append("*");
                sb.append(c);
                sb.append(" ");
                i++;
            }
            System.out.println(sb.toString());
        }
    }
}
