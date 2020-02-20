'''
965.单值二叉树
如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。

只有给定的树是单值二叉树时，才返回 true；否则返回 false。

示例 1：

输入：[1,1,1,1,1,null,1]
输出：true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/univalued-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []
        def dfs(node):
            if node:
                res.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)

        return len(set(res)) == 1

    def isUnival(self,root):
        left_res = ((not root or root.val ==root.left.val) and(self.isUnival(root.left)))
        right_res = ((not root or root.val ==root.right.val) and(self.isUnival(root.right)))

        return left_res and right_res