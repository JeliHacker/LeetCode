// https://leetcode.com/problems/add-two-numbers/description/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode();
        ListNode cur = dummy;
        int carry = 0;

        while (l1 != null || l2 != null || carry > 0)
        {
            int value1;
            int value2;

            if (l1 != null)
            {
                value1 = l1.val;
                l1 = l1.next;
            } else {
                value1 = 0;
            }
            if (l2 != null)
            {
                value2 = l2.val;
                l2 = l2.next;
            } else {
                value2 = 0;
            }

            int value = (value1 + value2 + carry) % 10;
            carry = (value1 + value2 + carry) / 10;

            cur.next = new ListNode(value);
            cur = cur.next;
        }

        Console.WriteLine(cur.val);
        return dummy.next;

    }
}
