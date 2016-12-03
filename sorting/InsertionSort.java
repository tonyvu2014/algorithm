public class InsertionSort implements SortOperation {
	@Override
	public void executeSort(int[] array) {
		int n = array.length;
		for (int i = 1; i < n; i++) {
			int x = array[i];
			int j = i-1;
			while (j>=0 && array[j]>x) {
				array[j+1] = array[j];
				j--;
			}
			array[j+1] = x;
		}
	}
}