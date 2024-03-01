// Input :
// 1  2  3  4

// 5  6  7  8

// 9 10 11 12

// 13 14 15 16

// Output :
// 4 8 12 16 15 11 7 3 2 6 10 14 13 9 5 1
public class WavePrint {
    public static void main(String[] args) {
        int array[][] = {
            {1,2,3,4},
            {5,6,7,8},
            {9,10,11,12},
            {13,14,15,16}
        };

        // for (int i = 0; i <array.length; i++) {
        //     for (int j = 0; j <array[i].length ; j++) {
        //         System.out.print(array[i][j]+ " ");
        //     }
        // }
        
        int startCol = 0,endCol=array.length -1,startRow = 0,endRow = array[0].length -1; 
        while(  startRow<endRow){
            for (int i = startCol; i <=endCol ; i++) {
                System.out.print(array[i][endRow] + " ");
            }
            endRow--;
            for (int i = endCol; i >= startCol; i--) {
                System.out.print(array[i][endRow] +" ");
            }
            endRow--;
        }
     
      
    }
  
}
