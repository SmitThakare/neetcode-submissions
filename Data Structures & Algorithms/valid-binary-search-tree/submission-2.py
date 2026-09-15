# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        result=[]
        def inorder(q):
            if not q:
                return 
            inorder(q.left)
            result.append(q.val)
            inorder(q.right)
        inorder(root)
        length=len(result)
        for i in range(length - 1):  # ← Stop before last element
            if result[i] >= result[i+1]:  # ← Check if NOT strictly increasing
                return False  # ← Only return False when found violation
        return True  # ← If loop completes, all pairs were valid
            