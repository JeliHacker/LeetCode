# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# answer = True
class Solution:
    
    answer = True
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverseTree(root1, root2):
            if root1 and root2:
                
                traverseTree(root1.left, root2.left)
                
                if root1.val != root2.val:
                    self.answer = False
                    return
                
                traverseTree(root1.right, root2.right)
                
            elif (not root1) and (not root2):
                pass
            else:
                self.answer = False
                return
                
        traverseTree(p, q)
        return self.answer
