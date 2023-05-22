"""
Given the head of a linked list, return the list after sorting it in ascending order.



Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105


Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:  # O(1) space and O(n log n) time
        if not head or not head.next:
            return head
        # Split to two lists
        left = head

        mid = self.__getMid(head)
        right = mid.next
        mid.next = None
        # Split to two lists

        return self.__merge_L_Lists(self.sortList(left), self.sortList(right))

    def __getMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def __merge_L_Lists(self, list1, list2):
        head = tail = ListNode()
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return head.next
