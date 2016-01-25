import java.io.*;
public class StringRotation{ 
    public static void main(String[] args) throws IOException{
        File file = new File("test_stringrotation.txt");
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while((line = buffer.readLine()) != null){
            line = line.trim();
            String parts[] = line.split(",");
            String doubstr = parts[0] + parts[0];
            String test = parts[1];
            int i = 0;    
            boolean found = false;
            while(i < doubstr.length()){    
                char d = doubstr.charAt(i);
                int j = 0, k = i;
                while(j < test.length() && k < doubstr.length() && doubstr.charAt(k) == test.charAt(j)){
                    j++;
                    k++;
                }
                if(j == test.length()){
                    found = true;
                    break;
                }
                i++;
            }
            if (found)
                System.out.println("True");
            else
                System.out.println("False");

        }
    }
}
