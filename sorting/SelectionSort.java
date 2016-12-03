public class SelectionSort implements SortOperation {
	@Override
	public void executeSort(int[] array) {
		int n = array.length;
		for (int i = 0; i < n-1; i++) {
			int min = i;
			for (int j = i+1; j < n; j++) {
				if (array[j]<array[min]) {
					min = j;
				}
			}
			
			exchange(array, min, i);
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