# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(root: Node):
            if not root:
                return
            # left traversal
            dfs(root.left)
            #
            if self.pre:
                self.pre.right, root.left = root, self.pre
            # pre is None means here is the head
            else:
                self.head = root
            # middle traversal, give the middle node to previous
            self.pre = root
            # right traversal
            dfs(root.right)

        if not root:
            return
        # init pre and head
        self.pre = None
        self.head = None
        dfs(root)
        # link the head and tail
        self.head.left, self.pre.right = self.pre, self.head
        # return the head
        return self.head
