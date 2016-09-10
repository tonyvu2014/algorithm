package search;

import java.util.*;

public class SearchExperiment {
		
	public static void main(String[] args) {
		
		int node_count = Integer.parseInt(args[0]);
		
		int[][] adjacentMatrix = initializeSparseGraph(node_count);
		
		System.out.println("Adjacent Matrix:");
		printMatrix(adjacentMatrix);
		
		System.out.println("Breath First Search Traversal: ");
		long startTime = System.currentTimeMillis();
	    
		breadthFirstSearch(adjacentMatrix, 0); 	
      
		long endTime = System.currentTimeMillis();
		System.out.println("Running Beadth First Search in: " + (endTime-startTime) + " ms");
		
		System.out.println();
		
		System.out.println("Depth First Search Traversal: ");
		startTime = System.currentTimeMillis();
	    
		depthFirstSearch(adjacentMatrix, 0); 	
      
		endTime = System.currentTimeMillis();
		System.out.println("Running Depth First Search in: " + (endTime-startTime) + " ms");	

	}
	
	
	private static int[][] initializeDenseGraph(int node_count) {
		int[][] adjacentMatrix = new int[node_count][node_count];
		
		Random random = new Random();
		for (int i = 0; i < node_count; i++) {
			for (int j = 0; j < node_count; j++) {
				if (i==j) {
					adjacentMatrix[i][j] = 0;
				} else {
				    adjacentMatrix[i][j] = random.nextInt(2);
			    }
			}
		}
		
		return adjacentMatrix;
	}
	
	
	private static int[][] initializeSparseGraph(int node_count) {
		int[][] adjacentMatrix = new int[node_count][node_count];
		
		Random random = new Random();
		for (int i = 0; i < node_count; i++) {
			for (int j = 0; j < node_count; j++) {
				if (i==j) {
					adjacentMatrix[i][j] = 0;
				} else {
				    adjacentMatrix[i][j] = random.nextInt(10)<2?1:0;
			    }
			}
		}
		
		return adjacentMatrix;
	}
	
	private static void printMatrix(int[][] matrix) {
		StringBuilder stringBuilder = new StringBuilder();
		for (int i = 0;i < matrix.length;i++) {
			for (int j = 0;j < matrix[i].length;j++) {
				stringBuilder.append(matrix[i][j] + "  ");
			}
			stringBuilder.append("\n");
		}
		System.out.println(stringBuilder);
	}
	
	private static void breadthFirstSearch(int[][] adjacentMatrix, int node) {
		Map<Integer, Boolean> visitedMap = new HashMap<Integer, Boolean>();
		for (int i=0;i <adjacentMatrix.length;i++) {
			visitedMap.put(i, false);
		}
		List<Integer> nodeQueue = new LinkedList<Integer>();
		nodeQueue.add(node);
		
		while (!nodeQueue.isEmpty()) {
			int currentNode = nodeQueue.remove(0);
			visitedMap.put(currentNode, true);
			
			System.out.println(currentNode);
			
			List<Integer> adjacentNodes = getAdjacentNodes(adjacentMatrix, currentNode);
			for (int n: adjacentNodes) {
				if (!visitedMap.get(n) && !nodeQueue.contains(n)) {
			        nodeQueue.add(n);
			    }
		    }
		}
		
	}
	
	private static List getAdjacentNodes(int[][] adjacentMatrix, int node) {
	    List<Integer> adjacentNodes = new LinkedList<Integer>();	
	
		int[] adjacentArray = adjacentMatrix[node];
		for (int j=0;j<adjacentArray.length;j++) {
			if (adjacentArray[j] == 1) {
				adjacentNodes.add(j);
			}
		}
		
		return adjacentNodes;
	}
	
	private static void depthFirstSearch(int[][] adjacentMatrix, int node) {
		Map<Integer, Boolean> visitedMap = new HashMap<Integer, Boolean>();
		for (int i=0;i <adjacentMatrix.length;i++) {
			visitedMap.put(i, false);
		}
		
		dfs(adjacentMatrix, node, visitedMap);
	}
	
	private static void dfs(int[][] adjacentMatrix, int node, Map<Integer, Boolean> visitedMap) {
		System.out.println(node);
		visitedMap.put(node, true);
		
		List<Integer> adjacentNodes = getAdjacentNodes(adjacentMatrix, node);
		for (int n: adjacentNodes) {
			if (!visitedMap.get(n)) {
				dfs(adjacentMatrix, n, visitedMap);
			}
		}
	}
	
	
}