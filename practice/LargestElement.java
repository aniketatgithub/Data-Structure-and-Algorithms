/*
 * Implement a function that takes vector of integers as input and returns the largest element.

Sample Input

-3 4 1 2 3

-1 -2 -3 -3 8

Sample Output

4

8

Explanation : for test case one, 4 is the largest integer in the array.

Similarly for test case two, 8 is the largest integer in the array.
 */

import java.util.Scanner;
import java.util.Vector;

public class LargestElement {
    public static void main(String[] args) {
        Vector<Integer> arr = new Vector<Integer>();
        // Add elements to the vector
        arr.add(1);
        arr.add(2);
        arr.add(3);
    //   Scanner scan = new Scanner(System.in);
    // for (int i = 0; i < arr.length; i++) {
    //     arr[i] =scan.nextLine();
    // }
    int max = 0;
    for (int j = 0; j < arr.size(); j++) {
        if(max < arr.get(j)) max = arr.get(j);
    }
        System.out.println(max);

    }
    
}
