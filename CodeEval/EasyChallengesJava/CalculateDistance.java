/*
 * Calculate distance between two points
 */
import java.io.*;
public class CalculateDistance{ 
    private static class Point{
        int x, y;
        public Point(int x, int y){
            this.x = x;
            this.y = y;
        }
        public int distanceTo(Point that){
            double x2, y2, distf;
            x2 = Math.pow((this.x - that.x),2.0);
            y2 = Math.pow((this.y - that.y),2.0);
            distf = Math.sqrt(x2+y2);
            return (int)distf;
        }
    }
    public static void main(String[] args) throws IOException{
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while((line = buffer.readLine()) != null){
            line = line.trim();
            String rem = "[() ,\n]+";
            String[] nums = line.replaceFirst("^\\(","").split(rem);
            Point p1 = new Point(Integer.parseInt(nums[0]), Integer.parseInt(nums[1]));
            Point p2 = new Point(Integer.parseInt(nums[2]), Integer.parseInt(nums[3]));
            System.out.println(p1.distanceTo(p2));
            
        }

    }
}
