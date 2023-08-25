//Print the sum of each subarray & find out the largest sum
//Comment off other classes to run seprately
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


//Way 2 : Prefix Sums
class LargestPrefixSum{
    
    public static void main(String[] args) {
        int arr[] = {1,2,3,4,5,6,-7};
        int lastSum = 0;
        int prefixArr[]={0,0,0,0,0,0,0};
        for (int i = 0; i < arr.length; i++) {
                    prefixArr[i] =  lastSum + arr[i];
                    lastSum = lastSum + arr[i];
        } 
        // to print sums array
        // for (int j = 0; j < arr.length; j++) {
        //     System.out.print(prefixArr[j] + " ");
        // }
        int maxSum =0;
        for (int i = 0; i < prefixArr.length; i++) {
            for (int j = i; j < prefixArr.length; j++) {
                if(prefixArr[j] - prefixArr[i] + arr[i]>maxSum){
                    maxSum = prefixArr[j] - prefixArr[i] + arr[i];
                }
            }
        }
        System.out.println(maxSum);
    }
}