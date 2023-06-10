'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_head = ListNode(0)
        result_cur = result_head
        carried_value = 0
        while l1 or l2 or carried_value:
            if l1:
                carried_value += l1.val
                l1 = l1.next

            if l2:
                carried_value += l2.val
                l2 = l2.next

            carried_value, current_value = divmod(carried_value, 10)

            result_cur.next = ListNode(current_value)
            result_cur = result_cur.next

        return result_head.next


    def print_result(self):
        l1 = ListNode(9,
                      ListNode(9,
                               ListNode(9,
                                        ListNode(9,
                                                 ListNode(9,
                                                          ListNode(9,
                                                                   ListNode(9
                                                                            )
                                                                   )
                                                          )
                                                 )
                                        )
                               )
                      )
        l2 = ListNode(9,
                      ListNode(9,
                               ListNode(9,
                                        ListNode(9)
                                        )
                               )
                      )

        result = self.addTwoNumbers(l1, l2)
        current = result
        while current is not None:
            print(current.val, end=' --> ')
            current = current.next
        print('None')


Solution().print_result()
