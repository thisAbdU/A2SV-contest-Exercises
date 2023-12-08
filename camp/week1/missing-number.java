class Solution {
    public int missingNumber(int[] nums) {
        Arrays.sort(nums);
        for(int i=0; i< nums.length; i++){
            if (Math.abs(nums[i] - i)== 1){
                return i;
            }
        }return nums.length;
    }
}