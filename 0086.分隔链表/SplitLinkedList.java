package leetcode;

public class SplitLinkedList {

    public ListNode partition(ListNode head, int x) {
        ListNode dummy = new ListNode(Integer.MIN_VALUE);
        dummy.next = head;
        ListNode node = head;
        ListNode prev = dummy;
        while (node != null && node.val < x) {
            node = node.next;
            prev = prev.next;
        }
        ListNode lastnode = prev;
        while (node != null) {
            if (node.val < x) {
                ListNode nextnode = node.next;

                ListNode lastNodeNext = lastnode.next;
                lastnode.next = node;
                node.next = lastNodeNext;
                lastnode = node;

                prev.next = nextnode;
                node = prev.next;
            } else {
                node = node.next;
                prev = prev.next;
            }
        }

        return dummy.next;
    }
}
