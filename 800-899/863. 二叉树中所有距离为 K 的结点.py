# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.parents = {}
        self.ans = []
        self.find_parents(root)
        self.find_ans(target, None, 0, k)
        return self.ans

    def find_parents(self, node: TreeNode):
        if node.left:
            self.parents[node.left.val] = node
            self.find_parents(node.left)
        if node.right:
            self.parents[node.right.val] = node
            self.find_parents(node.right)

    def find_ans(self, root: TreeNode, origin: TreeNode, depth: int, distance: int):
        if not root:
            return
        if depth == distance:
            self.ans.append(root.val)
            return
        if root.left != origin:
            self.find_ans(root.left, root, depth + 1, distance)
        if root.right != origin:
            self.find_ans(root.right, root, depth + 1, distance)
        if self.parents.get(root.val) != origin:
            self.find_ans(self.parents.get(root.val), root, depth + 1, distance)
