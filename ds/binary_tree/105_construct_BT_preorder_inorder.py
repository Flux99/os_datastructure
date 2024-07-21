# Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        print("root.left",preorder[1:mid+1],inorder[:mid])
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        print("root.right",preorder[mid+1:],inorder[mid+1:])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root


# root.left [9] [9]
# root.left [] []
# root.right [] []
# root.right [20, 15, 7] [15, 20, 7]
# root.left [15] [15]
# root.left [] []
# root.right [] []
# root.right [7] [7]
# root.left [] []
# root.right [] []