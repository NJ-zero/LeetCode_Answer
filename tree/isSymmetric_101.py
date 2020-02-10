'''
101.对称二叉树
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路：

'''
class Solution(object):
    def isSymmetric(self, root):
        """
        采用递归
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(left,right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            return dfs(left.left,right.right) and dfs(left.right,right.left)

        return dfs(root.left,root.right)

    def isSymmetric(self, root):
        '''
        采用迭代,改用队列实现
        首先从队列中拿出两个节点(left和right)比较
        将left的left节点和right的right节点放入队列
        将left的right节点和right的left节点放入队列
        :param root:
        :return:
        '''
        if not root or not(root.left or root.right):
            return True

        queue = [root.left,root.right]

        while queue:
            left = queue.pop(0)
            right = queue.pop(0)
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False

            queue.append(left.left)
            queue.append(right.right)

            queue.append(left.right)
            queue.append(right.left)
        return True