# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.max_sum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def max_gain(node):
            if not node:
                return 0
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            price_new_path = node.val + left_gain + right_gain

            self.max_sum = max(self.max_sum, price_new_path)

            return node.val + max(left_gain, right_gain)

        max_gain(root)

        return self.max_sum
