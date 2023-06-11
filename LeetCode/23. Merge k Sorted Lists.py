"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""
# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Time complexity : O(Nlogk) where k is the number of linked lists.
    We can merge two sorted linked lists in O(n) time when n is the total number of nodes in two lists.
    """

    def mergeKLists_Recursive(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Takes O(nk) space for recursion stack"""
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            return self.mergeTwoLists(lists[0], lists[1])

        # Divide and Conquer
        mid = len(lists) // 2
        left_half = self.mergeKLists_Recursive(lists[:mid])
        right_half = self.mergeKLists_Recursive(lists[mid:])
        return self.mergeTwoLists(left_half, right_half)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Iterative approach -> O(1) space"""
        if not lists:
            return None

        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                second_list = lists[i + 1] if i + 1 < len(lists) else None
                temp.append(self.mergeTwoLists(lists[i], second_list))
            lists = temp
        return lists[0]

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Space complexity : O(1) We can merge two sorted linked lists in O(1) space while excluding result space
        """
        result = ListNode()
        cur = result
        p, q = list1, list2
        while p and q:
            if p.val < q.val:
                cur.next = p
                p = p.next
            else:
                cur.next = q
                q = q.next
            cur = cur.next
        cur.next = p if p else q
        return result.next


obj = Solution()
l1 = ListNode(1,
              ListNode(4,
                       ListNode(5)))
l2 = ListNode(1,
              ListNode(3,
                       ListNode(4)))
l3 = ListNode(2,
              ListNode(6))
# l1,l2 = ListNode(), ListNode()
output = obj.mergeKLists_Recursive([l1, l2, l3])
current = output
while current is not None:
    print(current.val, end=' --> ')
    current = current.next
print('None')
