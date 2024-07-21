# Leetcode link: https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Leetcode 124. Binary Tree Maximum Path Sum
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxval = [root.val]

        def dfs(node):
            if node is None:
                return 0
            leftmax = max(0,dfs(node.left))
            rightmax = max(0,dfs(node.right))
            maxval[0] = max(maxval[0], rightmax + leftmax + node.val)
            return node.val + max(leftmax,rightmax) 
        
        dfs(root)
        return maxval[0]

        