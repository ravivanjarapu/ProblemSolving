"""
Given a binary tree, determine if it is
height-balanced
.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced_slow(self, root: Optional[TreeNode]) -> bool:
        result = True
        if root:

            def get_height(node):
                if not node:
                    return True
                nonlocal result
                left_height = get_height(node.left)
                right_height = get_height(node.right)

                if not abs(left_height - right_height) in (0, 1):
                    result = result and False
                return 1 + max(left_height, right_height)

            left_child_height = get_height(root.left)
            right_child_height = get_height(root.right)
            result = result and ((left_child_height - right_child_height) in (-1, 0, 1))
        return result

    def isBalanced_faster(self, root: Optional[TreeNode]) -> bool:
        """Same time complexity as above. But no overhead of maintaining result"""
        def get_height(node):
            if not node:
                return 0
            left_height = get_height(node.left)
            if left_height == -1:
                return -1
            right_height = get_height(node.right)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1
            return 1 + max(left_height, right_height)

        return get_height(root) != -1
