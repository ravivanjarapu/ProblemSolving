"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root:
            q = deque()
            q.append(root)
            left_to_right = True

            while q:
                sub_result = []
                qLen = len(q)
                for _ in range(qLen):
                    node = q.popleft()
                    if node:
                        sub_result.append(node.val)
                        q.append(node.left)
                        q.append(node.right)

                if sub_result:
                    if not left_to_right:
                        sub_result.reverse()
                    result.append(sub_result)
                left_to_right = not left_to_right
        return result
