# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import defaultdict


class Solution:
    def __init__(self):
        self.ans = 0

    def pathSum(self, root: TreeNode, sum: int) -> int:
        cache = defaultdict(int)
        cache[0] += 1
        self.dfs(root, cache, 0, sum)
        return self.ans

    def dfs(self, root, cache, pre_presum, target):
        if not root:
            return

        pre_sum = pre_presum + root.val
        sub = pre_sum - target
        if sub in cache:
            self.ans += cache[sub]
        cache[pre_sum] += 1
        
        """
        # cache里面只有简单的数据结构，直接浅拷贝就行，这样就不需要在后面减一（cache[pre_sum] -= 1)
        # 有同学有疑问这里会什么要用深浅拷贝或者在后面减1:
        # 比如，这里从当前层先进入left子树，left子树会将它的pre_sum加入cache中，
        # 当left子树返回后，再从当前层进入右子树时带上了左子树的pre_sum信息，这样程序就不对了
        """
        self.dfs(root.left, cache.copy(), pre_sum, target)
        self.dfs(root.right, cache.copy(), pre_sum, target)
