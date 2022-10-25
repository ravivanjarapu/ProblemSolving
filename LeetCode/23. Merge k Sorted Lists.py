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
    Complexity Analysis

    Time complexity : O(Nlogk) where k is the number of linked lists.

    We can merge two sorted linked list in O(n) time where n is the total number of nodes in two lists.
    Space complexity : O(1)

    We can merge two sorted linked lists in O(1) space.
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            return self.mergeTwoLists(lists[0], lists[1])

        # Divide and Conquer
        mid = len(lists) // 2
        left_half = self.mergeKLists(lists[:mid])
        right_half = self.mergeKLists(lists[mid:])
        return self.mergeTwoLists(left_half, right_half)

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
              ListNode(4,
                       ListNode(5)))
l2 = ListNode(1,
              ListNode(3,
                       ListNode(4)))
l3 = ListNode(2,
              ListNode(6))
# l1,l2 = ListNode(), ListNode()
output = obj.mergeKLists([l1, l2, l3])
current = output
while current is not None:
    print(current.val, end=' --> ')
    current = current.next
print('None')
