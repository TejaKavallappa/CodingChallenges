import java.io.*;
import java.util.Scanner;

public class StackImplement{ 
    private static int size;
    private static Node head;

    private static class Node{
        int data;
        Node next;
        public Node(int data){
            this.data = data;
        }
    }

    StackImplement(){
        this.head = null;
        this.size = 0;
    }
    private static void push(int num){
        Node n = new Node(num);
        n.next = head;
        head = n;
        size++;    
    }
    private static int pop(){
        if(!isEmpty()){
            int out = head.data;
            head = head.next;
            size--;
            return out;
        }
        else
            return Integer.MIN_VALUE;
    }
    public static boolean isEmpty(){
        return (head == null);
    }
    public static void main(String[] args){
        try{
            Scanner reader = new Scanner(new File("test_stack.txt"));
            while (reader.hasNext()){
                StackImplement nstack = new StackImplement(); 
                String line = reader.nextLine();
                String[] nums = line.split(" ");
                //Add the numbers to the Stack
                for (String value : nums){
                    int num = Integer.parseInt(value);
                    nstack.push(num);
                }
                while(!nstack.isEmpty()){
                    System.out.print(nstack.pop() + " ");
                    int discard = nstack.pop();
                }
                System.out.println();
            }
        }
        catch(FileNotFoundException e){
            System.out.println("Unable to find file");
        }

    }
}
