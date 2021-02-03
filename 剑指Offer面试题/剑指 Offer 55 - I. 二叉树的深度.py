# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def max_depth_bfs(self, root: TreeNode) -> int:
        from collections import deque
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        res = 0
        while queue:
            n = len(queue)
            for i in range(n):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res += 1
        return res
