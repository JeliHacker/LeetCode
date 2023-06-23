# https://leetcode.com/problems/reorder-list/description/

# Definition for singly-linked list.

import copy

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderlist(head) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    prev = None
    slow.next = None

    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp


    # merge two halfs
    first = head
    second = prev
    while second:
        tmp1 = first.next
        tmp2 = second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2
        
    curr = copy.deepcopy(head)
    
    while curr:
        print(curr.val)
        curr = curr.next
        
        
my_head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
        
reorderlist(my_head)
        
