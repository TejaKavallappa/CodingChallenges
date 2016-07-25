import java.io.*;
public class SumOfIntegersFromFile{ 
    public static void main(String[] args) throws IOException{
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        int num, sum = 0;
        while((line = buffer.readLine()) != null){
            line = line.trim();
            num = Integer.parseInt(line);
            sum += num;
        }
        System.out.println(sum);
    }
}
