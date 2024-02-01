class Solution {
    public int sumOddLengthSubarrays(int[] arr) {
        int sum = 0;
        for(int i = 0; i < arr.length; i++){
            int left = i + 1;
            int right = arr.length - i;
            int num_subarrays = left * right;
            int odd_subarrays = num_subarrays%2 == 0 ? num_subarrays/2 : num_subarrays/2 + 1;
            sum += odd_subarrays * arr[i];
        }
        return sum;
    }
}