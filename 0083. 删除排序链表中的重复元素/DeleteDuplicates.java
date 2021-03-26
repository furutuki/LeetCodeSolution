/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return null;
        }
        ListNode dummyNode = new ListNode(0);
        dummyNode.next = head;
        ListNode prev = dummyNode.next;
        ListNode node = head.next;
        while (node != null) {
            if (prev.val == node.val) {
                node = node.next;
                prev.next = node;
            } else {
                prev = node;
                node = node.next;
            }
        }
        return dummyNode.next;

    }
}