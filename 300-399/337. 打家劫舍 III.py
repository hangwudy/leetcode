# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        sel, unsel = self.dfs(root)
        return max(sel, unsel)

    def dfs(self, root: TreeNode):
        if not root:
            return [0, 0]
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        sel = root.val + l[1] + r[1]
        unsel = max(l[0], l[1]) + max(r[0], r[1])
        return [sel, unsel]
