"""
Given the root of a binary tree, invert the tree, and return its root.



Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree_recursion(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """This is bottom up"""
        if not root:
            return None

        left_child = self.invertTree_recursion(root.left) if root.left else None
        right_child = self.invertTree_recursion(root.right) if root.right else None
        root.left, root.right = right_child, left_child
        return root

    def invertTree_iteration_top_down(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """This is top down. Faster than recursion"""
        if not root:
            return None
        q = deque([root])
        while q:
            cur = q.popleft()
            cur.left, cur.right = cur.right, cur.left
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        return root

    def invertTree_iteration_bottom_up(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """This is bottom up
        I think this is best because we don't need t import deque and is iterative"""
        if not root:
            return None
        stack = [root]
        while stack:
            cur = stack.pop()

            cur.left, cur.right = cur.right, cur.left
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return root
