# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base case: empty arrays
        if not preorder or not inorder:
            return None
        
        # Step 1: Root is first element of preorder
        root = TreeNode(preorder[0])
        
        # Step 2: Find root's position in inorder
        mid = inorder.index(preorder[0])
        
        # Step 3: Recursively build left and right
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root