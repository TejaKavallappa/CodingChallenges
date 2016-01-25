import java.util.Scanner;

public class PascalsTriangle{ 
    public static int[][] pascal(int depth) {
        int[][] sol = new int[depth][];
        sol[0] = new int[]{1};
        sol[1] = new int[]{1, 1};
        for(int i = 2; i < depth; i++){
            sol[i] = new int[i+1];
            for(int j = 1; j < i; j++){
                sol[i][j] = sol[i-1][j-1] + sol[i-1][j];
            }
            sol[i][i] = 1;
            sol[i][0] = 1;
        }
        return sol;
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the depth: ");
        int depth = scanner.nextInt();
        int[][] res = new int[depth][];
        res = pascal(depth);

        for(int i = 0; i < res.length; i++){
            for(int j = 0; j < res[i].length; j++){
                System.out.print(res[i][j]+ " ");
            }
            System.out.println();
        }
    }
}
