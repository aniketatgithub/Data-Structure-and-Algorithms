package neetcode;

public class ValidPalindrom {
//32
        public static boolean isPalindrome(String s) {
            String asciiChar = "";
            int arr[] = new int[26];
      
            for (int i = 0; i < s.length(); i++) {
               if(s.charAt(i) - 'a' < 27 && s.charAt(i) - 'a'>=0 || s.charAt(i) - 'A' < 27 && s.charAt(i) - 'A'>=0){
                    if(s.charAt(i) - 'A' < 27 && s.charAt(i) - 'A'>=0){
                       
                        s = s.substring(0, i) + Character.toLowerCase(s.charAt(i)) + s.substring(i+1);
                    }
                    asciiChar = asciiChar + s.charAt(i);
               } 
            }
            System.out.println(asciiChar);
            //abab

            for (int j = 0; j < (asciiChar.length()); j++) {
                    arr[asciiChar.charAt(j)-'a']++;   
            }
            for (int i = 0; i < arr.length; i++) {
                 System.out.print(arr[i] + " ");
            }
            // Capital letter are 32 --
           
             for (int j = 0; j < asciiChar.length(); j++) {
                arr[asciiChar.charAt(j)-'a']--;   
             }

            for (int i = 0; i < arr.length; i++) {
                if(arr[i]!=0){
                    return false;
                }
            }

            return true;
        }
        public static void main(String[] args) {
           System.out.println((isPalindrome("ABab"))); 
        }
}
