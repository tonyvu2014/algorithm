import java.util.Arrays;

public class MergeSort implements SortOperation {
	@Override
	public void executeSort(int[] array) {
        mergeSort(array, 0, array.length-1);
    }

    private void mergeSort(int[] array, int low, int high) {
        if (low < high) { 
            int middle = (low + high)/2;

            mergeSort(array, low, middle);
            mergeSort(array, middle+1, high);

            merge(array, low, middle, high);
        } 
    }

    private void merge(int[] array, int low, int middle, int high) {

        int[] helperArray = Arrays.copyOf(array, array.length);

        int i = low;
        int j = middle+1;
        int k = low;

        while (i <= middle && j <=high) {
            if (helperArray[i] < helperArray[j]) {
                array[k] = helperArray[i];
                i++;
            } else {
                array[k] = helperArray[j];
                j++;
            }
            k++;
        }

        int remaining = middle - i;
        for (int s = 0; s <= remaining; s++) {
            array[k+s] = helperArray[i + s];
        }
    }
}