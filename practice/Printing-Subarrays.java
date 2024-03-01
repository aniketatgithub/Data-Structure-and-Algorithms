//Find All the Subarrays of a Given Array in Java
class Subarrays {
    
    public static void main(String[] args) {
            int arr[] = {1,2,3,4,5,6,7};
            for (int i = 0; i < arr.length; i++) {
                for (int j = i+1; j < arr.length; j++) {
                    for (int j2 = i; j2 < j; j2++) {
                       System.out.print(" (" + arr[j2] + "),");
                    }
                      System.out.println("");
                }
                System.out.println("");
            }
    }
}