public class BubbleSort {

    public int[] bubleSort(int[] nums){
        boolean swapped = false;

        for (int i = 0; i < nums.length; i++) {
           for (int j = 1; j < nums.length - i; j++) {
              if (nums[j] < nums[j-1]) {
                int temp = 0;
                temp = nums[j-1];
                nums[j-1] = nums[j];
                nums[j] = temp;

                swapped = true;
              }
           }

           if(!swapped){
            break;
           }
        }

        return nums;
    }
}