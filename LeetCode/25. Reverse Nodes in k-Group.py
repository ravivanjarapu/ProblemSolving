"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]


Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000


Follow-up: Can you solve the problem in O(1) extra memory space?
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
            Recursion takes O(n) space for recursion stack
            Iteration take O(1) space
            https://leetcode.com/problems/reverse-nodes-in-k-group/editorial/ - Both recursion and iteration
        """

        '''# Recursion
        k_count, cur = 0, head

        while cur and k_count < k:  # Works until k > 0
            cur = cur.next
            k_count += 1

        if k == k_count:
            reversed_head = self.reverseList_upto_k_nodes(head, k)
            head.next = self.reverseKGroup(cur, k)
            return reversed_head
        return head'''

        # Iteration
        cur, new_head, k_tail = head, None, None
        while cur:
            k_count, cur = 0, head
            while cur and k_count < k:  # Works until k > 0
                cur = cur.next
                k_count += 1  # Stops cur at k+1st node or None

            if k == k_count:  # If full set of k nodes are available. If not, outer while loop exits too.
                reversed_head = self.reverseList_upto_k_nodes(head, k)
                if not new_head:
                    new_head = reversed_head
                if k_tail:
                    k_tail.next = reversed_head
                k_tail = head
                head = cur
        if k_tail:
            k_tail.next = head

        return new_head if new_head else head

    def reverseList_upto_k_nodes(self, head: Optional[ListNode], k) -> Optional[ListNode]:
        new_head, cur = None, head
        while k:
            temp = cur.next
            cur.next = new_head
            new_head = cur
            cur = temp
            k -= 1
        return new_head
