public class CyclicSort {

    public int[] cyclicSortMethod(int[] nums){
        for (int i = 0; i < nums.length; i++) {
            if (nums[nums[i] - 1] != nums[i]) {
                swap(nums,nums[i] - 1, i);
            }
        
        }return nums;
    }

    static void swap(int[] nums, int first, int second){
        int temp = nums[first];
        nums[first] = nums[second];
        nums[second] = temp;
    }
}