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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result = new ListNode(0);
        int carry = 0;
        int temp = 0;
        int x ;
        int y ;
        ListNode curr = result;
        while( l1 != null || l2!= null){
            if (l1 != null){
                x = l1.val;
            } else{
                x = 0;
            }
            if (l2 != null){
                 y = l2.val;
            }else{
                y = 0;
            }
            temp = x + y + carry;
            carry = 0;
            if(temp >= 10){
                carry = 1;
                temp -= 10;
            }
            curr.next =  new ListNode(temp);
            curr = curr.next;
            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }
    if (carry > 0) {
        curr.next = new ListNode(carry);
    }
    return result.next;
    }
}
