# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.queue = deque()
        self.inorder(root)

    def inorder(self, root: TreeNode):
        if not root:
            return
        self.inorder(root.left)
        self.queue.append(root.val)
        self.inorder(root.right)

    def next(self) -> int:
        return self.queue.popleft()

    def hasNext(self) -> bool:
        return len(self.queue) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
