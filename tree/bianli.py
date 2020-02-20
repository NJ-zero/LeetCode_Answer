'''
二叉树的遍历
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bianli(self, root):
        '''
        前序遍历
        :param root:
        :return:
        '''
        if not root:
            return None
        print(root.val)
        self.bianli(root.left)
        self.bianli(root.right)
