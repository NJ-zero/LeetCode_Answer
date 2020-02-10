'''
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路：

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        采用递归的方式
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth,right_depth)+1

    def maxDepth2(self, root):
        '''
        DFS
        :param root:
        :return:
        '''
        stack =[]
        if root is not None:
            stack.append((1,root))
        depth = 0
        while stack != []:
            cur_depth,root = stack.pop()
            if root is not None:
                depth = max(depth,cur_depth)
                stack.append((depth+1,root.left))
                stack.append((depth+1,root.right))

        return depth