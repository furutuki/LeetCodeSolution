public class OddEventList {
    public ListNode oddEvenList(ListNode head) {
        ListNode odd, even;
        if (head == null || head.next == null) {
            return head;
        }

        ListNode eventHead;
        odd = head;
        even = head.next;
        eventHead = even;
        while (true) {
            if (even.next != null) {
                odd.next = even.next;
                odd = odd.next;
                even.next = null;
            } else {
                odd.next = eventHead;
                break;
            }

            if (odd.next != null) {
                even.next = odd.next;
                even = even.next;
                odd.next = null;
            } else {
                odd.next = eventHead;
                break;
            }
        }

        return head;
    }

    public static void main(String[] argv) {
        ListNode n1 = new ListNode(1);
        ListNode n2 = new ListNode(2);
        ListNode n3 = new ListNode(3);
        ListNode n4 = new ListNode(4);
        ListNode n5 = new ListNode(5);
        ListNode n6 = new ListNode(6);
        ListNode n7 = new ListNode(7);
        ListNode n8 = new ListNode(8);

        n1.next = n2;
        n2.next = n3;
        n3.next = n4;
        n4.next = n5;
        n5.next = n6;
        n6.next = n7;
        n7.next = n8;
        n8.next = null;

        ListNode ans = new OddEventList().oddEvenList(n1);
        System.out.println(ans);
    }
}

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}
