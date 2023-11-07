//23.

import java.util.Scanner;
import java.util.Vector;

public class MaximumSubarraySum {
    public static void main(String[] args) {
                Scanner scan = new Scanner(System.in);
                System.out.println("Enter the size of vector: ");
                int size = scan.nextInt();
                System.out.println("Enter the elemets : ");
                Vector<Integer> vector = new Vector<>();
                for (int i = 0; i < size; i++) {
                    vector.add(i, scan.nextInt());
               }
            //    for (int i = 0; i < vector.size(); i++) {
            //         System.out.println(vector.get(i));
            //    }
                int maxElement = Integer.MIN_VALUE;
                Boolean isAllnegative = true;
                for (int i = 0; i < vector.size(); i++) {
                    if(vector.get(i)>0){
                        isAllnegative = false;
                    }
                    if(maxElement<vector.get(i)){
                        maxElement = vector.get(i);
                    }
                }
               if(isAllnegative){
               System.out.println("Allnegative is true " + maxElement) ;
            }
            int max = 0; int curr = 0 ;
            //kadane's Algorithm
               for (int i = 0; i < vector.size(); i++) {
                    curr = curr + vector.get(i); 
                    if(curr<0){ curr = 0;  }
                    if(curr > max) {  max = curr;}
               }
 System.out.println(max) ;

    }
}
