# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        stack = []
        stack.append(root)
        total_sum = 0

        while stack:
            current_node = stack.pop()
            
            if current_node.left:
                if current_node.left.left is None and current_node.left.right is None:
                    total_sum += current_node.left.val
                else:
                    stack.append(current_node.left)
            if current_node.right:
                stack.append(current_node.right)

        return total_sum