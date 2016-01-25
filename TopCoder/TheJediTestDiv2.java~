import java.util.*;
public class TheJediTestDiv2{
	public static int countSupervisors(int[] students, int Y, int J){
		Arrays.sort(students);
		int largest = students[students.length-1];
		if((largest-Y)<0)
			students[students.length-1]=0;
		else students[students.length-1]=largest-Y;
		int numJedis =0;
		for(int floorStudents:students){
			int floorJedis =  (int) Math.ceil(floorStudents/(J*1.0));
			numJedis += floorJedis;
			System.out.println(floorJedis);

		}
		return numJedis;
	}
	public static void main(String[] args){
		int[] students = {11,13,15};
		int Y = 9;
		int J = 5;
		System.out.println(countSupervisors(students, Y,J));
	}
}
