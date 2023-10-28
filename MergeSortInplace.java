import java.util.Arrays;

public class MergeSortInplace {

    public void mergeSortInPlaceMethod(int[] arr, int start, int end) {
        if (end - start > 1) { 
            int mid = (start + end) / 2; 

            mergeSortInPlaceMethod(arr, start, mid);
            mergeSortInPlaceMethod(arr, mid, end);

            merge(arr, start, mid, end);
        }
    }

    static void merge(int[] arr, int start, int mid, int end) {
        int i = start;
        int j = mid;
        int k = 0;

        int[] merged = new int[end - start];

        while (i < mid && j < end) {
            if (arr[i] < arr[j]) {
                merged[k] = arr[i];
                i++;
            } else {
                merged[k] = arr[j];
                j++;
            }
            k++;
        }
        while (i < mid) {
            merged[k] = arr[i];
            i++;
            k++;
        }
        while (j < end) {
            merged[k] = arr[j];
            j++;
            k++;
        }

        for (int l = 0; l < merged.length; l++) {
            arr[start + l] = merged[l];
        }
    }

   
}
