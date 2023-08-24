import java.util.Vector;

public class LowerBound {
    public static void main(String[] args) {
        Vector<Integer> vec = new Vector<Integer>();
        vec.add(1);
        vec.add(2);
        vec.add(3);
        vec.add(4);
        System.out.println(checknum(vec));
      
    }

    public static int checknum(Vector<Integer> vec){
           int target  = 3;
          for (int i = 0; i < vec.size(); i++) {
            if(target== vec.get(i)){
                return target;
            }
            else if(target<vec.get(i)){
                if(i!=0){
                return vec.get(i-1);
                }else{
                    return -1;
                }
                    
            }
        }
        return 0;
    }
}
