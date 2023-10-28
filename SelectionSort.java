public class SelectionSort {

    public int[] selectionSortMethod(int[] nums) {
        for (int i = 0; i < nums.length - 1; i++) {
            int last = nums.length - i - 1;
            int maximumIndex = getMaximumIndex(nums, 0, last);
            swap(nums, maximumIndex, last);

            // for decreasing order
            // int minimumIndex = getMinimumIndex(nums, 0, last); 
            // swap(nums, last, minimumIndex);
        }
        return nums;
    }

    static int getMaximumIndex(int[] nums, int start, int last) {
        int maximum = start;

        for (int i = start; i <= last; i++) {
            if (nums[i] > nums[maximum]) {
                maximum = i;
            }
        }
        return maximum;
    }

    static int getMinimumIndex(int[] nums, int start, int last){
        int minimum = start;

        for (int i = 0; i <= last; i++) {
            if (nums[i] < nums[minimum]) {
                minimum = i;
            }
        }
        return minimum;
    }

    static void swap(int[] nums, int first, int second) {
        int temp = nums[first];
        nums[first] = nums[second];
        nums[second] = temp;
    }
}
