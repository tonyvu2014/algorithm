import java.util.Arrays;
import java.util.Random;

public class SortExperiment {	
	public static void main(String[] args) {
		int n = 50000;
		int min_value = -500000;
		int max_value = 500000;
		Random random =  new Random();
		
		int[] array = new int[n];
		for (int i = 0; i < n; i++) {
			array[i] = random.nextInt(max_value-min_value+1) + min_value;
		}
		
		
		int[] array1 = Arrays.copyOf(array, array.length);
		SortAlgorithm sortAlgorithm = new SortAlgorithm(new QuickSort());
		long startTime = System.currentTimeMillis();
		sortAlgorithm.sort(array1);
		long endTime = System.currentTimeMillis();
		System.out.println("Running QuickSort in: " + (endTime-startTime) + " ms");
		
		int[] array2 = Arrays.copyOf(array, array.length);
		sortAlgorithm = new SortAlgorithm(new HeapSort());
		startTime = System.currentTimeMillis();
		sortAlgorithm.sort(array2);
		endTime = System.currentTimeMillis();
		System.out.println("Running HeapSort in: " + (endTime-startTime) + " ms");
		
		int[] array3 = Arrays.copyOf(array, array.length);
		sortAlgorithm = new SortAlgorithm(new InsertionSort());
		startTime = System.currentTimeMillis();
		sortAlgorithm.sort(array3);
		endTime = System.currentTimeMillis();
		System.out.println("Running InsertionSort in: " + (endTime-startTime) + " ms");
		
		int[] array4 = Arrays.copyOf(array, array.length);
		sortAlgorithm = new SortAlgorithm(new SelectionSort());
		startTime = System.currentTimeMillis();
		sortAlgorithm.sort(array4);
		endTime = System.currentTimeMillis();
		System.out.println("Running SelectionSort in: " + (endTime-startTime) + " ms");
		
		int[] array5 = Arrays.copyOf(array, array.length);
		sortAlgorithm = new SortAlgorithm(new BubbleSort());
		startTime = System.currentTimeMillis();
		sortAlgorithm.sort(array5);
		endTime = System.currentTimeMillis();
		System.out.println("Running BubbleSort in: " + (endTime-startTime) + " ms");

	}
	
}