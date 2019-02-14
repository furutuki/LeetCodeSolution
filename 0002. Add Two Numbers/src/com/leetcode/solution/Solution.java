package com.leetcode.solution;

import java.math.BigInteger;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

public class Solution {
	
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    	BigInteger total = new BigInteger("0");
    	
    	total = addNumbers(total, l1);
    	total = addNumbers(total, l2);

    	String str = new StringBuilder(total.toString()).reverse().toString();
    	return createNumber(str);
    }

    public static void main(String[] args) {
    	ListNode l1 = createNumber("243");
    	ListNode l2 = createNumber("564");
    	ListNode list = new Solution().addTwoNumbers(l1, l2);
    	ListNode node = list;
    	while (node != null) {
    		System.out.print(node.val + " ");
    		node = node.next;
    	}
    }
    
    private BigInteger addNumbers(BigInteger total, ListNode list) {
    	StringBuilder sb = new StringBuilder();
    	for (ListNode node = list; node != null; node = node.next) {
    		sb.append(node.val);
    	}
    	return total.add(new BigInteger(sb.reverse().toString()));
    }
    
    private static ListNode createNumber(String str) {
    	ListNode headNode = null;
    	ListNode tailNode = null;
    	for (int i = 0; i < str.length(); i++) {
    		ListNode tmpNode = new ListNode(str.charAt(i) - '0');
    		if (tailNode == null) {
    			headNode = tmpNode;
    			tailNode = tmpNode;
    			tailNode.next = null;
    		} else {
    			tailNode.next = tmpNode;
    			tailNode = tmpNode;
    		}
    	};
    	return headNode;
    }
}