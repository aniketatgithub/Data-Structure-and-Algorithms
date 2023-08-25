import java.util.Scanner;
import java.util.Vector;

public class LowerBound {
    //BRUTEFORCE

    // public static void main(String[] args) {
    //     Vector<Integer> vec = new Vector<Integer>();
    //     vec.add(1);
    //     vec.add(2);
    //     vec.add(3);
    //     vec.add(4);
    //     System.out.println(checknum(vec));
      
    // }

    // public static int checknum(Vector<Integer> vec){
    //        int target  = 3;
    //       for (int i = 0; i < vec.size(); i++) {
    //         if(target== vec.get(i)){
    //             return target;
    //         }
    //         else if(target<vec.get(i)){
    //             if(i!=0){
    //             return vec.get(i-1);
    //             }else{
    //                 return -1;
    //             }
                    
    //         }
    //     }
    //     return 0;
    // }


    //OPTIMISED USING CUSTOMISED BINARY SEARCH

    public static void main(String[] args) {
        Vector<Integer> vector = new Vector<>();
        System.out.println("Enter the size of Vector");
        Scanner scan = new Scanner(System.in);
        int vectorSize = scan.nextInt();
        System.out.println("Enter the elements : ");
        for (int i = 0; i < vectorSize; i++) {
            vector.add(i,scan.nextInt());
        }
         System.out.println("Enter the target value : ");
         int target = scan.nextInt();
        //Printing vector
        // for (int j = 0; j < vectorSize; j++) {
        //     System.out.println(vector.get(j));
        // }
        int j2=0;int mid =vectorSize/2;int s =0;int end = vectorSize-1;int ans = -1;
        while( j2<vectorSize -1 ){
            mid = (s + end)/2;
            System.out.println(" MID : " + vector.get(mid));
            if(vector.get(mid)<=target){
                if(vector.get(mid) == target){
                    ans = vector.get(mid);
                    System.out.println("Found : " + ans );
                    System.exit(0);
                }else{
                      s = mid+1;
                }
            }else{
                end = mid - 1;
            }
            j2++;
        }
        System.out.println(ans);

    }
}
