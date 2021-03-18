package leetcode;

public class ReverseBetween {

    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode dummyNode = new ListNode();
        dummyNode.next = head;
        ListNode prev = dummyNode;
        for (int idx = 1; idx < left; idx++) {
            prev = prev.next;
        }

        ListNode node = prev.next;
        for (int i = left; i < right; i++) {
            ListNode nextnode = node.next;
            node.next = nextnode.next;
            nextnode.next = prev.next;
            prev.next = nextnode;
        }

        return dummyNode.next;
    }
}
