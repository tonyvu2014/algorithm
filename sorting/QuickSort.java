public class QuickSort implements SortOperation {
	@Override
	public void executeSort(int[] array) {
		quickSort(array, 0, array.length-1);
	}
	
	private void quickSort(int[] array, int startIndex, int endIndex) {
		if (startIndex < endIndex) {
			int pivotIndex = partition(array, startIndex, endIndex);
			quickSort(array, startIndex, pivotIndex-1);
			quickSort(array, pivotIndex, endIndex);
		}
	}
	
	private int partition(int[] array, int p, int q) {
		int pivotValue = array[q];
		int currentIndex = p;
		for (int i=p; i<=q-1; i++) {
			if (array[i] <= pivotValue) {
				exchange(array, i, currentIndex);
				currentIndex++;
			}
		}
		exchange(array, currentIndex, q);
		
		return currentIndex;		
	}
	
	private void exchange(int[] array, int i, int j) {
		if (i == j) {
			return;
		}
		int tmp = array[i];
		array[i] = array[j];
		array[j] = tmp;
	}
}