# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        left_nodes = self.mirrorTree(root.right)
        right_nodes = self.mirrorTree(root.left)
        root.left = left_nodes
        root.right = right_nodes
        return root
