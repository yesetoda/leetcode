# Inorder Traversal
def inorder(root,out = []):
    if root is None:
        return

    stack = []
    current_node = root
    

    while True:
        if current_node is not None:
            stack.append(current_node)
            current_node = current_node.left
        elif stack:
            current_node = stack.pop()
            out.append(current_node.value, end=' ')
            current_node = current_node.right
        else:
            break
    return out



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> list[int]:
        out= []
        return sorted(inorder(root2,inorder(root1,out)))