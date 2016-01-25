import java.io.*;
import java.util.Scanner;
public class CardNumberValidation{ 
    public static void main(String[] args){
        try{
            Scanner readfile = new Scanner(new File("test_cardnumvalidation.txt"));
            String line;
            while(readfile.hasNext()){
                line = readfile.nextLine().trim();
                line = line.replaceAll("\\s","");
                int digits[] = new int[line.length()];
                int second, sum = 0;
                if (digits.length % 2 == 0){
                    second = 0;
                }
                else
                    second = 1;
                for (int i = 0; i < line.length(); i++){
                    digits[i] = Character.getNumericValue(line.charAt(i));
                    
                    if (i == second){
                        int num = digits[i]*2;
                        if(num > 9){
                            num = 1 + (num%10);
                        }
                        second = second+2;
                        digits[i] = num;
                    }
                }
                
                for (int i :digits){
                    sum += i;
                }

                if (sum % 10 == 0)
                    System.out.println("1");
                else
                    System.out.println("0");
            }
        }
        catch(FileNotFoundException e){
            System.out.println("File not found"); 
        }
    }

}
