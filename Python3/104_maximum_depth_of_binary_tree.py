# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maximumDepth(root):
            if not root:
                return 0
            maxLeft = maximumDepth(root.left)
            maxRight = maximumDepth(root.right)

            return max(maxLeft, maxRight) + 1
    
        return maximumDepth(root)
