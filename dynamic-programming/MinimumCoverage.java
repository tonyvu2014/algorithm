/***
Given an digit array of size n
Find the minimum number of consecutive elements in the array that 
contain all the values of that array
*/

import java.util.Collections;

public class MinimumCoverage {
	
	private static final int[] A = new int[]{1, 3, 0, 7, 4, 3, 5, 4, 1, 9, 7}; 
	
	public static void main(String[] args) {
		System.out.println(findMinimumCoverage(A));
	}
	
	public static int findMinimumCoverage(int[] a) {
		
		int n = a.length;
		
		String[][] coverageSet =  new String[n][n];
		int[][] coverageCount =  new int[n][n];
		
		
		for (int i = 0; i < n; i++) {
			coverageSet[i][i] = ""+a[i];
			coverageCount[i][i] = 0;
		}
		
		int maxCoverageCount = 0;
		int coverageRange = n;
		
		for (int i=0; i < n-1; i++) {
			for (int j=i+1; j < n; j++) {
				coverageSet[i][j] = new String(coverageSet[i][j-1]);
				coverageCount[i][j] = coverageCount[i][j-1];
				if (!coverageSet[i][j-1].contains(""+a[j])) {
					coverageSet[i][j] += a[j];
					coverageCount[i][j] += 1;
				}
				if (coverageCount[i][j] > maxCoverageCount) {
					maxCoverageCount = coverageCount[i][j];
					coverageRange = j - i + 1; 
				}
			}
		}	 
		
		return coverageRange;
	}
}