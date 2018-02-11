/**
 * Given an integer n and an array of k integers a1, a2,...,ak 
 * For the range of number from 0 to n-1, we perform the following steps:
 * - Remove all multiples of a1: 0, a1, 2*a1,... and so on
 * - Remove all multiples of a1: 0, a2, 2*a2,... and so on 
 * - And so on for a3 to ak
 * 
 * - Return the number of integers that are remained after these operations
 */

import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class RemainingNumbers {

	private static final Integer[] a = new Integer[]{3,3,7,5};
	
	public static void main(String[] args) {
		System.out.println(countRemainingNumbers(100, a));
	}
	
	static int countRemainingNumbers(int n, Integer[] a) {
        Set<Integer> cleanSet = new TreeSet<>();
        for (int e: a) {
            cleanSet.add(e);
        }
		
		Map<Integer, Boolean> removed = new HashMap<>();
		for (int i = 0; i < n; i++) {
			removed.put(i, false);
		}
		int remainingCount = n;
		for (int jumpNumber : cleanSet) {
			System.out.println("Jump Number: " + jumpNumber);
			int i = 0;
			while (jumpNumber*i < n) {
				if (!removed.get(jumpNumber*i)) {
					removed.put(jumpNumber*i, true);
					remainingCount--;
				}
				i++;
			}
		}
		
		return remainingCount;
	}
}
