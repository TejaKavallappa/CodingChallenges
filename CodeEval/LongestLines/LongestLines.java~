import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import java.util.PriorityQueue;
import java.util.Comparator;
import java.util.Collections;

public class LongestLines{ 
public static void main(String[] args){
    try{
        Scanner file = new Scanner(new File("longestLinesTest.txt"));
        int sizePQ = Integer.parseInt(file.next());
       // Comparator<String> lineComparator = (String s1, String s2)->Integer.compare(s1.length(),(s2.length()));
        Comparator<String> lineComparator = new Comparator<String>(){
            @Override
                public int compare(String s1, String s2){
                    return Integer.compare(s1.length(), s2.length());
                }
        };
        Comparator<String> reverseLineComparator = new Comparator<String>(){
            @Override
                public int compare(String s1, String s2){
                    return Integer.compare(s2.length(), s1.length());
                }
        };
        PriorityQueue<String> longLines = new PriorityQueue<String>(sizePQ,lineComparator );
        String line;
        while(file.hasNext()){
            line = file.nextLine().trim();
            longLines.add(line);
            System.out.println(line+ " " + line.length());
            
        }
        while(longLines.size()>sizePQ){
            System.out.println(longLines.poll().length());
        }
        System.out.println(longLines.size());

        PriorityQueue<String>reversed = new PriorityQueue<String>(longLines.size(),reverseLineComparator);
        reversed.addAll(longLines);
        System.out.println("Printing lines in descending order\n");
        while(reversed.size()>0){
            System.out.println(reversed.poll());
        }
    }
    catch(IOException e){
        System.out.println("Unable to open file.");
    }
}

}
