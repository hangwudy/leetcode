# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.pre = None
        self.head = None

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self.dfs(root)
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head

    def dfs(self, root: 'Node'):
        if not root:
            return None
        self.dfs(root.left)
        if self.pre:
            self.pre.right = root
            root.left = self.pre
        else:
            self.head = root
        self.pre = root
        self.dfs(root.right)
