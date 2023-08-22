//This takes O(n) time to find the max sum of subarrays
public class KadaneAlgotithm {
    public static void main(String[] args) {
        int curr = 0,max =0;
        int arr[] = {-2,3,4,-1,5,-12,6,1,3};
        for (int i = 0; i < arr.length; i++) {
            curr = curr + arr[i];
            if(curr < 0) curr = 0;
            if(curr>max) max = curr;
        }
        System.out.println(max);
    }
}
