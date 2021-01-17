# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.max_dia = 0
        self.depth(root)
        return self.max_dia - 1

    def depth(self, root: TreeNode):
        if not root:
            return 0
        dl = self.depth(root.left)
        dr = self.depth(root.right)
        self.max_dia = max(self.max_dia, dl + dr + 1)
        return max(dl, dr) + 1
