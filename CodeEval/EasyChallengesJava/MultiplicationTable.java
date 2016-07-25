/*
 * Print out multiplication table upto 12*12
 */
public class MultiplicationTable{ 
    public static void main(String[] args){
        for(int j = 1; j <= 12; j++){
            for(int i = 1; i <= 12; i++){
                System.out.format("%4d",i*j);
            }
            System.out.println();
        }
    }
    
}
