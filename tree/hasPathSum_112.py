'''
112.路径总和
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        利用栈，进行迭代
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        res=[(root,sum-root.val)]
        while res:
            node,cur_sum = res.pop()
            if not root.left and not root.right and cur_sum == 0:
                return True
            if node.right:
                res.append((root.right,cur_sum-root.right.val))
            if node.left:
                res.append((root.left,cur_sum-root.left.val))

        return False

    def has_Path_Sum(self, root, sum):
        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:
            return sum == 0

        return self.has_Path_Sum(root.left, sum) or self.has_Path_Sum(root.right, sum)