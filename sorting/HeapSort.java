public class HeapSort implements SortOperation {
	@Override
	public void executeSort(int[] array) {
		int n = array.length;
		int heapSize = n;
		buildMaxHeap(array);
		for (int i = n-1; i > 0; i--) {
			int temp = array[i];
			array[i] = array[0];
			array[0] = temp;
			heapSize--;
			maxHeapify(array, heapSize, 0);
		}
	}
	
	private void maxHeapify(int[] array, int heapSize, int index) {
		int leftIndex = 2*index+1;
		int rightIndex = 2*index+2;
		int biggestIndex = index;
		if (leftIndex < heapSize) {
			if (array[leftIndex] > array[index]) {
				biggestIndex = leftIndex;
			} else {
				biggestIndex = index;
			}
		}
		
		if (rightIndex < heapSize) {
			if (array[rightIndex] > array[biggestIndex]) {
				biggestIndex = rightIndex;
			}
		}
		
		if (biggestIndex != index) {
			exchange(array, biggestIndex, index);
			maxHeapify(array, heapSize, biggestIndex);
		}
		
	}
	
	private void buildMaxHeap(int[] array) {
		int heapSize = array.length;
		for (int i = heapSize/2; i >= 0; i--) {
			maxHeapify(array, heapSize, i);
		}
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