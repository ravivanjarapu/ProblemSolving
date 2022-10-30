"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


Follow up: Could you do this in one pass?
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        p, q = head, head
        while q.next is not None and n > 0:
            q = q.next
            n -= 1
        if q.next is None and n > 0:
            return head.next
        print('q:', q.val)
        while q.next is not None:
            p, q = p.next, q.next
        print('p, q: ', p.val, q.val)
        p.next = p.next.next
        return head


obj = Solution()
h = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
output = obj.removeNthFromEnd(h, 2)
# h = ListNode(1)
# h = ListNode(1, ListNode(2))
# output = obj.removeNthFromEnd(h, 1)
current = output
while current is not None:
    print(current.val, end=' --> ')
    current = current.next
print('None')
