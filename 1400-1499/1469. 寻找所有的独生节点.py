from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return
        if root.left and not root.right:
            self.res.append(root.left.val)
            self.dfs(root.left)
        elif not root.left and root.right:
            self.res.append(root.right.val)
            self.dfs(root.right)
        else:
            self.dfs(root.left)
            self.dfs(root.right)
