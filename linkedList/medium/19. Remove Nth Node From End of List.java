import linkedList.ListNode;

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // the distance between fast and slow is n+1
        // then slow should be in front of the deleting node
        ListNode dummy = new ListNode(0, head);
        ListNode fast = dummy, slow = dummy;
        for (int i = 0; i <= n; i++) {
            fast = fast.next;
        }

        while (fast != null) {
            slow = slow.next;
            fast = fast.next;
        }

        // delete the target
        slow.next = slow.next.next;

        return dummy.next;
    }
}