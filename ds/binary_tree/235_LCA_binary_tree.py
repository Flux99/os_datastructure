# 235. Lowest Common Ancestor of a Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root

        while curr:
            if curr.val <  p.val and curr.val <  q.val:
                curr= curr.right
            if curr.val >  p.val and curr.val >  q.val:
                curr= curr.left
            else:
                return curr
