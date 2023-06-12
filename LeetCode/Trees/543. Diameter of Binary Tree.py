"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.



Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1


Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        all_heights = {}

        def get_height(node):
            if node and node not in all_heights:
                left_child_height = all_heights.setdefault(node.left, get_height(node.left))
                right_child_height = all_heights.setdefault(node.right, get_height(node.right))
                all_heights[node] = 1 + max(left_child_height, right_child_height)
            return all_heights.get(node, 0)

        left_height, right_height = get_height(root.left), get_height(root.right)
        current = left_height + right_height
        return max(current,
                   self.diameterOfBinaryTree(root.left),
                   self.diameterOfBinaryTree(root.right))
