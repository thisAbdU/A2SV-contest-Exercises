import java.util.ArrayList;
import java.util.List;

class LuckyStarship{
    public int luckyNumber(int num1, int num2){
      int max = Integer.MIN_VALUE;
      
      while (num2 - num1 >= 0 ) {
        String numStr = Integer.toString(num1);
        int[] digits = new int[numStr.length()];

        for (int i = 0; i < digits.length; i++) {
            digits[i] = numStr.charAt(i);
        }
        for (int i = 0; i < digits.length; i++) {
            if (max < digits[i]) {
                max = digits[i];
            }
        
        }
      }
        return 1;
    }
}