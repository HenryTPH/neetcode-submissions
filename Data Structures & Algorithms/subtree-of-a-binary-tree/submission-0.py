# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root: 
            return False
        
        temp = subRoot
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if self.isSameTree(node, temp):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
        
    def isSameTree(self, p: TreeNode | None, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        left_check = self.isSameTree(q.left, p.left)
        right_check = self.isSameTree(p.right, q.right)
        return left_check and right_check
        