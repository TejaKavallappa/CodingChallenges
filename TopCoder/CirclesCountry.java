import java.util.ArrayList;
public class CirclesCountry{
	private static ArrayList<Circle> circles = new ArrayList<Circle>();
	private static class Circle{
		int xCord, yCord;
		int radius;
		public Circle(int xCord, int yCord, int radius){
			this.xCord = xCord;
			this.yCord = yCord;
			this.radius = radius;
		}
	}
	public static int leastBorders(int[] X, int[] Y, int[] R, int x1,int y1, int x2, int y2){
		for(int i=0;i<X.length;i++){
			Circle newCircle = new Circle(X[i],Y[i],R[i]);
			circles.add(newCircle);
		}
		ArrayList<Circle> boundaries = new ArrayList<Circle>();
		for(Circle circle:circles){
			//Check if pt P1 lies inside circle
				int lhs = ((circle.xCord - x1)*(circle.xCord-x1))+((circle.yCord-y1)*(circle.yCord-y1));
				if (lhs <= (circle.radius*circle.radius)){
					boundaries.add(circle);
				}

			//Check if pt P2 lies inside circle
				int lhsP2 = ((circle.xCord - x2)*(circle.xCord-x2))+((circle.yCord-y2)*(circle.yCord-y2));
				if ((lhsP2 <= (circle.radius*circle.radius))){
					if (boundaries.contains(circle))
						boundaries.remove(circle);
					else boundaries.add(circle);
				}
		}
		return boundaries.size();
	}
	public static void main(String[] args){
		int[] X = {-107,-38,140,148,-198,172,-179,148,176,153,-56,-187};
		int[] Y = {175,-115,23,-2,-49,-151,-52,42,0,68,109,-174};
		int[] R = {135,42,70,39,89,39,43,150,10,120,16,8};
		int x1 = 102,y1=16,x2=19,y2=-108;
		System.out.println(leastBorders(X,Y,R,x1,y1,x2,y2));
	}
}
