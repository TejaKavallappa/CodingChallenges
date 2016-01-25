import java.io.*;
import java.util.Scanner;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class PointInCircle{ 
    private class Point{
        public double x, y;
        public Point(double[] xy){
            this.x = xy[0];
            this.y = xy[1];
        }
        public double distTo(Point that){
            double dist;
            dist = (this.x - that.x)*(this.x- that.x) + (this.y - that.y)*(this.y-that.y);
            dist = Math.sqrt(dist);
            return dist;
        }
    }
    public static void main(String[] args) throws IOException{
        Scanner readfile = new Scanner(new File("test_pointincircle.txt"));
        String line;
        while(readfile.hasNextLine()){
            line = readfile.nextLine();
            line = line.trim();
            String parts[] = line.split(";");
            //Parse center
            Pattern p = Pattern.compile("\\-?\\d+\\.?\\d*");
            Matcher m = p.matcher(parts[0]);
            double[] xy = new double[2];
            int i = 0;
            while(m.find()){
                xy[i++] = Double.parseDouble(m.group(0)); 
            }
            Point center = new PointInCircle().new Point(xy);
            //Parse radius
            Pattern q = Pattern.compile("\\d+\\.?\\d*");
            Matcher n = q.matcher(parts[1]);
            double radius = 0;
            if (n.find()){
                radius = Double.parseDouble(n.group(0));
            }

            //Parse point
            Matcher o = p.matcher(parts[2]);
            i = 0;
            while(o.find()){
                xy[i++] = Double.parseDouble(o.group(0));
            }
            Point pt = new PointInCircle().new Point(xy);

            System.out.println(center.distTo(pt) + " " + radius);
            System.out.println(center.distTo(pt)<=radius);
        }

    }
}
