"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderRecursiveTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Recursive traversal"""
        result = []
        if root is not None:
            result.extend(self.inorderRecursiveTraversal(root.left))
            result.append(root.val)
            result.extend(self.inorderRecursiveTraversal(root.right))

        return result

    @staticmethod
    def inorderIterativeTraversal(root: Optional[TreeNode]) -> List[int]:
        """Iterative traversal
        Time complexity: O(n)   Space complexity:   O(n)
        """
        result = []
        stack = []
        node = root
        while True:
            while node:
                stack.append(node)
                node = node.left
            if len(stack) > 0:
                node = stack.pop()
                result.append(node.val)
                node = node.right
            else:
                break
        return result

    def inorderIterativeTraversal_Morris(self, root: Optional[TreeNode]) -> List[int]:
        """
        Morris traversal -  Time complexity: O(n)   Space complexity:   O(1)
        https://www.youtube.com/watch?v=Oejc-PVd5ig
        """
        result = []
        cur = root
        while cur:
            if cur.left:
                predecessor = cur.left
                while predecessor.right and predecessor.right != cur:
                    predecessor = predecessor.right
                if not predecessor.right:
                    predecessor.right = cur
                    cur = cur.left
                else:
                    predecessor.right = None
                    result.append(cur.val)
                    cur = cur.right
            else:
                result.append(cur.val)
                cur = cur.right
        return result

