public class BinarySearch2D {

    static int[] search(int[][] nums, int target){
        int row = 0;
        int column = nums[0].length - 1;

        while (row < nums.length && column >= 0) {
            if (nums[row][column] == target){
                return new int[]{row, column};
            }
            if (nums[row][column] < target){
                row++;
            }else{
                column--;
            }
        }return new int[]{-1, -1};
    }
}