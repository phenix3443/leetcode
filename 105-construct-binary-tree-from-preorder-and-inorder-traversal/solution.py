from typing import List, Optional
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """从前序与中序遍历序列构造二叉树"""

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return

        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)
        # 因为不管在inorder还是preorder，idx+1前面都是root及其子树的节点
        root.left = self.buildTree(preorder[1 : idx + 1], inorder[:idx])
        root.right = self.buildTree(preorder[idx + 1 :], inorder[idx + 1 :])

        return root


class TestBuildTree(unittest.TestCase):
    def compareTwoNode(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:  # 两个都不存在
            return True

        if p is None or q is None:  # 只有一个存在
            return False

        if p.val != q.val:  # 两个都存在，但是值不相等
            return False

        left = self.compareTwoNode(p.left, q.left)

        right = self.compareTwoNode(p.right, q.right)

        return left and right

    def test_1(self):
        node1 = TreeNode(3)
        node2 = TreeNode(9)
        node3 = TreeNode(20)
        node4 = TreeNode(15)
        node5 = TreeNode(7)

        node1.left = node2
        node1.right = node3
        node3.left = node4
        node3.right = node5
        target = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
        self.assertTrue(self.compareTwoNode(target, node1))


if __name__ == "__main__":
    unittest.main()
