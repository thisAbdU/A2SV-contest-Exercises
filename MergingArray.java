public class MergingArray {

    public int[] mergeSortedArrays(int m, int n, int[] num1, int[] num2) {
        int i = 0;
        int j = 0;
        int k = 0;
        int[] mergedArray = new int[m + n];

        while (i < m && j < n) {
            if (num1[i] <= num2[j]) {
                mergedArray[k] = num1[i];
                i++;
            } else {
                mergedArray[k] = num2[j];
                j++;
            }
            k++;
        }

        // Copy any remaining elements from num1 and num2
        while (i < m) {
            mergedArray[k] = num1[i];
            i++;
            k++;
        }
        
        while (j < n) {
            mergedArray[k] = num2[j];
            j++;
            k++;
        }

        return mergedArray;
    }
}
