"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        else:
            result = ListNode()
            r = result
            p, q = list1, list2
            while p and q:
                # print("p.val: %d, q.val: %d" % (p.val, q.val))
                if p.val < q.val:
                    r.next = p
                    p = p.next
                else:
                    r.next = q
                    q = q.next
                r = r.next
            r.next = p if p else q
        return result.next



obj = Solution()
l1 = ListNode(1,
              ListNode(2,
                       ListNode(4)))
l2 = ListNode(1,
              ListNode(3,
                       ListNode(4)))
# l1,l2 = ListNode(), ListNode()
output = obj.mergeTwoLists(l1, l2)
current = output
while current is not None:
    print(current.val, end=' --> ')
    current = current.next
print('None')
