/***
Given an integer array of size n
Find the minimum number of consecutive elements in the array that 
contain all the values of that array
*/

import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.HashSet;

public class MinimumCoverage {
	
	private static final int[] A = new int[]{1, 3, 0, 7, 4, 3, 5, 4, 1, 9, 7}; 
	
	public static void main(String[] args) {
		System.out.println(findMinimumCoverage(A));
	}
	
	public static int findMinimumCoverage(int[] a) {
		
		int n = a.length;
		
		Map<Integer, Set<Integer>> coverageMap =  new HashMap<Integer, Set<Integer>>();
		
		Set<Integer> allValues =  new HashSet<Integer>();
		
		for (int i = 0; i < n; i++) {
			allValues.add(a[i]);
			Set<Integer> s = new HashSet<Integer>();
			s.add(a[i]);
			coverageMap.put(i*n+i, s);
		}
		
		int valueCount = allValues.size();
		int minCoverageRange = n;
		
		for (int i = 0; i < n-1; i++) {
			for (int j =i + 1; j < n; j++) {
				Set<Integer> s = new HashSet<Integer>();
			    s.addAll(coverageMap.get(i*n+j-1));	
				s.add(a[j]);
				coverageMap.put(i*n+j, s);
				if (s.size() == valueCount && j-i+1 < minCoverageRange) {
					minCoverageRange = j-i+1;
				}
			}
		}	 
		
		return minCoverageRange;
	}
}