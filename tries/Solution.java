/***
We're going to make our own Contacts application! The application must perform two types of operations:

- add name, where  is a string denoting a contact name. This must store  as a new contact in the application.

- find partial, where  is a string denoting a partial name to search the application for. It must count the number of contacts 
starting with  and print the count on a new line.

Given  sequential add and find operations, perform each operation in order.

Input Format:

The first line contains a single integer, , denoting the number of operations to perform. 
Each line  of the  subsequent lines contains an operation in one of the two forms defined above.

Constraints:

It is guaranteed that  and  contain lowercase English letters only.
The input doesn't have any duplicate  for the  operation.

Output Format:

For each find partial operation, print the number of contact names starting with  on a new line.

Sample Input:

4
add hack
add hackerrank
find hac
find hak

Sample Output:

2
0

Explanation:

We perform the following sequence of operations:

Add a contact named hack.
Add a contact named hackerrank.
Find and print the number of contact names beginning with hac. There are currently two contact names in the application and both of them start with hac, so we print  on a new line.
Find and print the number of contact names beginning with hak. There are currently two contact names in the application but neither of them start with hak, so we print  on a new line.
***/
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
		Trie trie = new Trie();
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
		List<Integer> results= new ArrayList<Integer>();
        for(int a0 = 0; a0 < n; a0++){
            String op = in.next();
            String contact = in.next();
			if (op.equals("add")) {
				trie.addWord(contact);
			} else {
				results.add(trie.findPartial(contact));
			}
        }
		
		for (int result: results) {
			System.out.println(result);
		}
    }
	
	private static class TrieNode {
	
		private Character ch;
		private Map<Character, TrieNode> children;
		private boolean isLeaf;
		private int wordCount;
	
		public TrieNode(Character ch) {
			this.ch = ch;
			this.children = new HashMap<Character, TrieNode>();
			this.wordCount = 0;
		}
	
		public Character getCh() {
			return this.ch;
		}
	
		public void setCh(Character ch) {
			this.ch = ch;
		}
	
		public void addChild(TrieNode node) {
			this.children.put(node.getCh(), node);
		
		}
	
		public Map<Character, TrieNode> getChildren() {
			return this.children;
		}
		
		public void setIsLeaf(boolean isLeaf) {
			this.isLeaf = isLeaf;
		}
		
		public boolean getIsLeaf() {
			return this.isLeaf;
		}
		
		public int getWordCount() {
			return this.wordCount;
		}
		
		public void setWordCount(int wordCount) {
			this.wordCount = wordCount;
		}
	
	}

	private static class Trie {
		private TrieNode root;
	
		public Trie() {
			this.root = new TrieNode(null);
		}
	
		public TrieNode getRoot() {
			return root;
		}
	
		public void setRoot(TrieNode root) {
			this.root = root;
		}
		
	
		public void addWord(String word) {
			Map<Character, TrieNode> children = root.getChildren();
			for (int i = 0; i < word.length(); i++) {
				Character ch = word.charAt(i);
				TrieNode node;
				if (!children.containsKey(ch)) {
					node = new TrieNode(ch);
					children.put(ch, node);
				} else {
					node = children.get(ch);
				}
				children = node.getChildren();
				node.setWordCount(node.getWordCount()+1);
				
				if (i == word.length()-1) {
					node.setIsLeaf(true);
				}
			}
		}
	
		public int findPartial(String partial) {
			Map<Character, TrieNode> children = root.getChildren();
			TrieNode node = root;
			for (int i = 0; i < partial.length(); i++) {
				Character ch = partial.charAt(i);
				if (!children.containsKey(ch)) {
					return 0;
				} else {
					node = children.get(ch);
					children = node.getChildren();
				}
			}
			return node.getWordCount();
		}
	}
	
}
