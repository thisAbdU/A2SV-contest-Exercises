import java.util.Arrays;

public class Swap{
    public static void main(String[] args) {
        int[] list = {1, 2, 3, 4, 5};
        Solution swapSolution = new Solution();
        swapSolution.SwapIndex(list, 3, 2);
        System.out.println(Arrays.toString(list));
    }
}
class Solution{
    private int temp;
    void SwapIndex(int[] list, int indexN, int indexM){
        temp = list[indexN];
        list[indexN] = list[indexM];
        list[indexM] = temp;
    }
}