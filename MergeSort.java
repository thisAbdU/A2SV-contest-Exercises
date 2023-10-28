import java.util.Arrays;

public class MergeSort {

    public int[] mergeSortMethod(int[] arr){
        
        if (arr.length <= 1) {
            return arr;
        }

        int mid = arr.length/2;

        int[] leftArr = mergeSortMethod(Arrays.copyOfRange(arr, 0, mid));
        int[] rightArr = mergeSortMethod(Arrays.copyOfRange(arr, mid, arr.length));

        return merge(leftArr, rightArr);
    }

    static int[] merge(int[] arrayOne, int[] arrayTwo){
        int i = 0;
        int j = 0;
        int k = 0;

        int[] merged = new int[arrayOne.length + arrayTwo.length];

        while (i < arrayOne.length && j < arrayTwo.length) {
            if(arrayOne[i] > arrayTwo[j]){
                merged[k] = arrayOne[i];
                i++;
            }else{
                merged[k] = arrayTwo[j];
                j++;
            }
            k++;
        }
        while (i < arrayOne.length) {
            merged[k] = arrayOne[i];
            i++;
            k++;
        }
        while (j < arrayTwo.length) {
            merged[k] = arrayTwo[j];
            j++;
            k++;
        }

        return merged;
    }
}