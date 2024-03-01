package neetcode;

public class ValidAnagram {
    public static boolean isAnagram(String s, String t) {
     
       int arr[] = new int[26];
        for (int i = 0; i < s.length(); i++) {
              arr[s.charAt(i)-'a']++;
        }
       for (int i = 0; i < t.length(); i++) {
            arr[t.charAt(i)-'a']--;
        }
        for (int j = 0; j < arr.length; j++) {
            if(arr[j]!=0){
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args) {
        String str = "anagram", str2 = "naasdasdgaram";
        System.out.println(isAnagram(str,str2));
    }
}
