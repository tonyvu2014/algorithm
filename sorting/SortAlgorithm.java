public class SortAlgorithm {
	private SortOperation sortOperation;
	
	public SortAlgorithm(SortOperation sortOperation) {
		this.sortOperation = sortOperation;
	}
	
	public void sort(int[] array) {
		sortOperation.executeSort(array);
	}
}