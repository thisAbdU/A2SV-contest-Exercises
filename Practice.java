import java.util.ArrayList;
import java.util.Scanner;

public class Practice{
    public static void main(String[] args) {
       ArrayList<ArrayList<Integer>> multiAr = new ArrayList<>();
       Scanner input = new Scanner(System.in);
    for(int i = 0; i < 5; i++){
        multiAr.add(new ArrayList<>());
    }
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            multiAr.get(i).add(input.nextInt());
        }
        System.out.println(); 
    }
    System.out.println(multiAr);
    input.close();
    }
}