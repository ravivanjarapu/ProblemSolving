"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2


Constraints:

The number of nodes in the tree is in the range [0, 104].
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
    def maxDepth_deque(self, root: Optional[TreeNode]) -> int:
        """BFS Solution - https://www.youtube.com/watch?v=hTM3phVI6YQ - NeetCode"""
        result = 0
        if root:
            q = deque()
            q.append(root)

            while q:
                qLen = len(q)
                for _ in range(qLen):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                result += 1
        return result

    def maxDepth_recursive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth_recursive(root.left),
                       self.maxDepth_recursive(root.right))
