class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        ans = -1
        rootval = root.val

        def dfs(root):
            nonlocal ans
            if not root:
                return
            if ans != -1 and root.val > ans:
                return
            if root.val > rootval:
                ans = root.val
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ans
