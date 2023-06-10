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
        right = head
        for _ in range(n):  # 1 <= n <= sz. So, never goes out of bounds
            right = right.next

        dummy = ListNode(0, head)  # Dummy node added before head https://www.youtube.com/watch?v=XVuQxVej6y8 - NeetCode
        left = dummy
        while right:
            left, right = left.next, right.next
        left.next = left.next.next  # Removing the next node after left
        return dummy.next


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
