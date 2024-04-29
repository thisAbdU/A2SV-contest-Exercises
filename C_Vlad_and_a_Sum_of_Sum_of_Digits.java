import java.util.Scanner;

public class C_Vlad_and_a_Sum_of_Sum_of_Digits {
    
    public static void main(String[] args) {
       Scanner input = new Scanner(System.in);
       int testCase = input.nextInt();
       for (int i = 0; i < testCase; i++) {
            int num = input.nextInt();
            totalSum(num);
       }
       input.close();
    }

    public static void totalSum(int num){
        Long[] prefix = new Long[(int)(2 * (Math.pow(10, 5) + 1))];
        prefix[0] = 0L;
        for(int i = 1; i <= 2 * (Math.pow(10, 5)); i++){
            prefix[i] = prefix[i - 1] + sumOfDigits(i);
        }
        System.out.println(prefix[num]);
    }

    public static int sumOfDigits(long number) {
        String numberAsString = Long.toString(number);
        int sum = 0;
        for (int i = 0; i < numberAsString.length(); i++) {
            sum += Character.getNumericValue(numberAsString.charAt(i));
        }
        return sum;
    }
}
