from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        res = []

        def helper(root):
            if not root:
                return []
            res.append(root.val)
            for c in root.children:
                helper(c)

        helper(root)
        return res
