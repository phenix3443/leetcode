from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        res = []

        def helper(root):
            if not root:
                return
            for c in root.children:
                helper(c)
            res.append(root.val)

        helper(root)
        return res
