# coding=utf-8
# Time: 2019-10-22-17:47 
# Author: dongshichao


'''
删除链表中的节点

我们删除一个节点会碰到什么问题？下面删除3

1 -> 2 -> 3 -> 4
1
但是我们没有2的指针，该怎么办呢？我们可以将3=3.next

1 -> 2 -> 4 -> 4
              del
1
2
这样我们通过删除4实现我们的操作。
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val
        node.next=node.next.next