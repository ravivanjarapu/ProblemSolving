"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.



Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Time complexity: O(N) since one has to visit each node.
        Space complexity: O(D) to keep the queues, where DDD is a tree diameter. Max level could contain up to N/2 nodes
        """
        q = deque()
        if root:
            q.append(root)
        result = []
        while q:
            q_len = len(q)
            for i in range(q_len):
                node = q.popleft()
                '''
                This won't work when root = [1,2,3,4] output will be [1, 3] while expected is [1, 3, 4]. here 4 is left 
                node of 2. i will be 0 and q_len will be 4 when this level is traversed in for loop. when i = 4, node 
                will be empty and result won't be appended
                if node:
                    if i == q_len - 1:
                        result.append(node.val)
                    q.append(node.left)
                    q.append(node.right)'''
                if i == q_len - 1:
                    result.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result
