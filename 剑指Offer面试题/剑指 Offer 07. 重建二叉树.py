from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        length = len(preorder)
        hash_map = dict()
        for i, v in enumerate(inorder):
            hash_map[v] = i
        return self.constructTree(preorder, 0, length - 1, inorder, 0, length - 1, hash_map)

    def constructTree(self, preorder: List[int], pre_start: int, pre_end: int,
                      inorder: List[int], in_start: int, in_end: int, hash_map: dict) -> TreeNode:
        if pre_start > pre_end:
            return None
        root_val = preorder[pre_start]
        root = TreeNode(root_val)
        if pre_start == pre_end:
            return root
        else:
            root_index = hash_map[root_val]
            left_nodes = root_index - in_start
            right_nodes = in_end - root_index
            left_tree = self.constructTree(preorder, pre_start + 1, pre_start + left_nodes,
                                           inorder, in_start, root_index - 1, hash_map)
            right_tree = self.constructTree(preorder, pre_end - right_nodes + 1, pre_end,
                                            inorder, root_index + 1, in_end, hash_map)
            root.left = left_tree
            root.right = right_tree
            return root
