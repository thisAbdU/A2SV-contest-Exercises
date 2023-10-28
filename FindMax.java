public class FindMax{
    public static void main(String[] args) {
        int[] list = {1, 12, 3, 4, 5};
        System.out.println(FindMaximuminRange(list, 2, 4));
    }
    static int FindMaximum(int[] list){
    int max = Integer.MIN_VALUE;
    for(int i = 0; i < list.length; i++){
        if (list[i] > max) max = list[i];
    }
    return max;
}

   static int FindMaximuminRange(int[] list, int startingPt, int endPt){
    int max = Integer.MIN_VALUE;
        for(int i = startingPt; i <= endPt; i++){
        if (list[i] > max) max = list[i];
    }
    return max;
    
}

}


