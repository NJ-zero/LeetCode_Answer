'''
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/same-tree

思路：
递归大法
先判断 p 和 q 有没有空
再判断 val 是否相等
以上都通过，进行递归对子节点进行相同的判断
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q :
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left,q.left) and self.isSameTree(p.left,q.left)