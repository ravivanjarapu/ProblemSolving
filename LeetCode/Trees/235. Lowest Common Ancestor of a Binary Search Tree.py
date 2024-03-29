"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”



Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2


Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor_recursion(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Time Complexity : O(N), where N is the number of nodes in the BST.
                            In the worst case we might be visiting all the nodes of the BST.

        Space Complexity: O(N). This is because the maximum amount of space utilized by the recursion stack would be N
                            since the height of a skewed BST could be N.
        """
        p_val, q_val, root_val = p.val, q.val, root.val
        if p_val == q_val:
            return p

        if p_val < root_val and q_val < root_val:
            result = self.lowestCommonAncestor_recursion(root.left, p, q)
        elif p_val > root_val and q_val > root_val:
            result = self.lowestCommonAncestor_recursion(root.right, p, q)
        else:
            result = root
        return result

    def lowestCommonAncestor_iteration(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Time Complexity : O(N) - Same as above
        Space Complexity : O(1)
        """
        p_val, q_val = p.val, q.val
        if p_val == q_val:
            return p

        node = root
        while node:
            root_val = node.val
            if p_val < root_val and q_val < root_val:
                node = node.left
            elif p_val > root_val and q_val > root_val:
                node = node.right
            else:
                return node
