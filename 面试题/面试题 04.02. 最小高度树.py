from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        return self.helper(low=0, high=n - 1, nums=nums)

    def helper(self, low, high, nums) -> TreeNode:
        if low > high:
            return
        mid = (high - low + 1) // 2 + low
        root_val = nums[mid]
        root = TreeNode(root_val)
        root.left = self.helper(low, mid - 1, nums)
        root.right = self.helper(mid + 1, high, nums)
        return root
