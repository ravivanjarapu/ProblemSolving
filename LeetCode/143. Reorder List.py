"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]


Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find mid - Slow and fast pointer approach
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        '''slow is mid. 
        If even 11 13 17 19 -> slow is at 13. If odd 11 13 17 19 20 -> slow is at 17. 
        In either case, our second half starts from slow.next'''

        # Reverse second half
        mid_head = slow.next
        slow.next = None  # Breaking the Linked list at mid_head
        second_ptr = None  # This is reversed new head. Same logic as 206. Reverse Linked list
        while mid_head:
            temp = mid_head.next
            mid_head.next = second_ptr
            second_ptr = mid_head
            mid_head = temp
        # second_ptr now has reversed new head

        # Merge first half and second half
        first_ptr = head
        while second_ptr:
            temp1, temp2 = first_ptr.next, second_ptr.next

            first_ptr.next = second_ptr
            second_ptr.next = temp1

            first_ptr, second_ptr = temp1, temp2
