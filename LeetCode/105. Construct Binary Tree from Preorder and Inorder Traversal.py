"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.



Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]


Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""
from typing import List, Optional
from unittest import TestCase, main


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder and inorder:
            root = TreeNode(preorder[0])
            root_position = inorder.index(root.val)

            root.left = self.buildTree(preorder[1:root_position+1], inorder[:root_position])
            root.right = self.buildTree(preorder[root_position+1:], inorder[root_position + 1:])
            return root
        else:
            return None


class SimpleTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.obj = Solution()

    def test1(self):
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        self.assertEqual(self.obj.buildTree(preorder, inorder), [3, 9, 20, None, None, 15, 7])

    def test2(self):
        preorder = [-1]
        inorder = [-1]
        self.assertEqual(self.obj.buildTree(preorder, inorder), [-1])

    # def test3(self):
    #     self.assertEqual(self.obj.numDecodings("06"), 0)
    #
    # def test4(self):
    #     self.assertEqual(self.obj.numDecodings("11106"), 2)


if __name__ == "__main__":
    main()
