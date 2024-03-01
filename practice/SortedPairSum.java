import java.util.Scanner;
import java.util.Vector;

public class SortedPairSum {
    public static void main(String[] args) {
        Vector<Integer> vector = new Vector<Integer>();
        System.out.println("Enter the size : ");
        Scanner scan = new Scanner(System.in);
        int vectorSize = scan.nextInt();
        for (int i = 0; i < vectorSize; i++) {
            vector.add(i,scan.nextInt());
        }
        for (int i = 0; i < vectorSize; i++) {
                System.out.print(vector.get(i));
        }
        System.out.println("Enter the target  : ");
        int  target = scan.nextInt();
        int s =0,end = vectorSize -1;
        int i=0;int sum =0; int startIndex = -1; int endIndex = -1;
        int maxDiff = Integer.MAX_VALUE;
        while(i<vectorSize){
            sum = vector.get(s) + vector.get(end);
            if(sum==target)
            {
                System.out.println("target exact found by summing " + s + " and " + end);
                System.exit(0);
            }
            else{
                if(sum-target<maxDiff){
                    maxDiff = sum-target;
                    startIndex = s; endIndex = end;
                    s++;
                }else{
                    end--;
                }
            }
            i++;
        }
        System.out.println("closest to target found " + startIndex + "and " +endIndex);
    }

}
