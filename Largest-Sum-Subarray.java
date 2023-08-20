//Print the sum of each subarray & find out the largest sum
class LargestSum{
    public static void main(String[] args) {
        int max =0; int tempSum = 0;
         int arr[] = {1,2,3,4,5,6,7};
            for (int i = 0; i < arr.length; i++) {
                tempSum = 0;
                for (int j = i; j < arr.length; j++) {
                    for (int j2 = i; j2 <= j; j2++) {
                        System.out.print(" (" + arr[j2] + "),");
                        tempSum+= arr[j2];
                    }
                    System.out.println("Total sum : " + tempSum );
                      System.out.println("");
                    if(max < tempSum) max = tempSum;
                    tempSum = 0;
                }
                System.out.println("");
            }
             System.out.println("max is " + max);
    }
}