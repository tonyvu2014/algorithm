public class BubbleSort implements SortOperation {
	@Override
	public void executeSort(int[] array) {
		int n = array.length;
		int l = n-1;
		boolean swapped = true;
		while (swapped) {
			swapped = false;
			for (int i = 1; i <= l; i++) {
				if (array[i-1] > array[i]) {
					exchange(array,i-1, i);
					swapped = true;
				}
			}
			l--;
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