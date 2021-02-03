from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        n = len(inorder)
        hm = dict()
        for i, v in enumerate(inorder):
            hm[v] = i
        return self.construct(inorder, 0, n - 1, postorder, 0, n - 1, hm)

    def construct(self, inorder: List[int], in_start: int, in_end: int,
                  postorder: List[int], post_start: int, post_end: int, hashmap: dict) -> TreeNode:
        if in_start > in_end:
            return
        root_val = postorder[post_end]
        root = TreeNode(root_val)
        if in_start == in_end:
            return root
        else:
            root_index = hashmap[root_val]
            left_nodes = root_index - in_start
            right_nodes = in_end - root_index
            root.left = self.construct(inorder, in_start, root_index - 1,
                                       postorder, post_start, post_start + left_nodes - 1,
                                       hashmap)
            root.right = self.construct(inorder, root_index + 1, in_end,
                                        postorder, post_end - right_nodes, post_end - 1,
                                        hashmap)
            return root
