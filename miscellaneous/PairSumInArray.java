/***
Given an array of integers and a number
Check if there are 2 elements in the array that add up to that number
***/

import java.util.*;

public class PairSumInArray {
	
	private static final int[] A = {2, -3, 5, 1, 3, 7};
	private static final int total = 11;
	
	public static void main(String[] args) {
		
		System.out.println(findPairSumInArray(A, total));
		
	}
	
	private static boolean findPairSumInArray(int[] array, int total) {
		
		int[] sorted_array = Arrays.copyOf(array, array.length);
	    Arrays.sort(sorted_array);
		
		int l = sorted_array.length;
		int firstIndex = 0;
		int secondIndex = l-1;
				
		while (firstIndex < secondIndex) {
			int sum = sorted_array[firstIndex] + sorted_array[secondIndex];
			if (sum == total) {
				return true;
			} else if (sum < total) {
				firstIndex++;
			} else {
				secondIndex--;
			}
		}
		
		return false;
		
	}
	
}