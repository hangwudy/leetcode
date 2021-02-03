from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        dq_tree = deque([root])
        dq_val = deque([root.val])
        while dq_tree:
            node = dq_tree.popleft()
            tmp = dq_val.popleft()
            if not node.left and not node.right:
                if tmp == sum:
                    return True
                continue
            if node.left:
                dq_tree.append(node.left)
                dq_val.append(tmp + node.left.val)
            if node.right:
                dq_tree.append(node.right)
                dq_val.append(tmp + node.right.val)
        return False

    def hasPathSum_dfs(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum_dfs(root.left, sum - root.val) or self.hasPathSum_dfs(root.right, sum - root.val)
