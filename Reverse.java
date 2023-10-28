import java.util.Arrays;

public class Reverse{
    public static void main(String[] args) {
        int[] list = {1, 2, 3, 2, 4, 8};
        reverseList(list);
    }
    static void swap(int[] list, int indexN, int indexM){
        int temp = list[indexN];
        list[indexN] = list[indexM];
        list[indexM] = temp;
    }
    static void reverseList(int[] list){
        int start = 0;
        int end = list.length - 1;
        while (start < end){
            swap(list, start, end);
            start++;
            end--;
        }
        System.out.println(Arrays.toString(list));
    }
}

