from math import gcd

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def insertGreatestCommonDivisors(self, head: [ListNode]) -> [ListNode]:
        p = head
        while p.next is not None:
            print(head.next.val)
            q = p.next
            n = ListNode(gcd(p.val, q.val), q)
            p.next = n
            p = q
        return head
    
solution = Solution()
example_input = ListNode(18, ListNode(6, ListNode(10, ListNode(3))))

example_output = solution.insertGreatestCommonDivisors(example_input)

example_output_list = []
while example_output:
    example_output_list.append(example_output.val)
    example_output = example_output.next
    
print(example_output_list)