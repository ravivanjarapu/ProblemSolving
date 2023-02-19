"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""
import collections
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # result = []
        # if root:
        #     result.append([root.val])
        #
        #     def traverse(node):
        #         sub_result = []
        #         if node is not None:
        #             if node.left is not None:
        #                 sub_result.append(node.left.val)
        #             if node.right is not None:
        #                 sub_result.append(node.right.val)
        #             if len(sub_result) > 0:
        #                 result.append(sub_result)
        #             traverse(node.left)
        #             traverse(node.right)
        #
        #     traverse(root)
        # return result
        result = []
        q = collections.deque()
        if root:
            q.append(root)

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
                result.append(sub_result)
        return result

