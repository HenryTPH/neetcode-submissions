# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        temp = root
        left_node = self.invertTree(temp.right)
        right_node = self.invertTree(temp.left)
        temp.left = left_node
        temp.right = right_node
        return temp