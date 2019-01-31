package com.leetcode.solution;

/**
 * Definition for singly-linked list. public class ListNode { int val; ListNode
 * next; ListNode(int x) { val = x; } }
 */

public class Solution2 {

	public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
		ListNode p = l1;
		ListNode q = l2;
		ListNode headNode = null;
		ListNode tailNode = null;
		int k = 0;
		while (p != null || q != null || k > 0) {
			int val1 = (p != null) ? p.val : 0;
			int val2 = (q != null) ? q.val : 0;
			int sum = val1 + val2 + k;
			ListNode tmpNode = new ListNode((sum) % 10);
			if (tailNode == null) {
				headNode = tmpNode;
				tailNode = tmpNode;
				tailNode.next = null;
			} else {
				tailNode.next = tmpNode;
				tailNode = tmpNode;
			}
			k = (sum >= 10 ? 1 : 0);
			if (p != null) {
				p = p.next;
			}
			if (q != null) {
				q = q.next;
			}
		}
		return headNode;
	}

	public static void main(String[] args) {
		ListNode l1 = createNumber("243");
		ListNode l2 = createNumber("564");
		ListNode list = new Solution2().addTwoNumbers(l1, l2);
		ListNode node = list;
		while (node != null) {
			System.out.print(node.val + " ");
			node = node.next;
		}
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
		}
		;
		return headNode;
	}
}
