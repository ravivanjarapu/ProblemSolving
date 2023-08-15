"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.



Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3


Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104


Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest_recursive(self, root: Optional[TreeNode], k: int) -> int:
        """Time complexity : O(N) to traverse all nodes in worst case.
            Space complexity : O(N) to maintain recursive stack and result_array"""
        def in_order_traversal(node):
            if len(result_array) < k and node:
                in_order_traversal(node.left)
                result_array.append(node.val)
                in_order_traversal(node.right)

        result_array = []
        in_order_traversal(root)
        return result_array[k - 1]

    def kthSmallest_iterative(self, root: Optional[TreeNode], k: int) -> int:
        # https://www.youtube.com/watch?v=5LUXSvjmGCw -> NeetCode
        stack, result_array = [], []
        node = root
        while True:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            result_array.append(node.val)
            if len(result_array) == k:
                return result_array[k-1]
            node = node.right
