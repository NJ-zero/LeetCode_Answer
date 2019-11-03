# coding=utf-8
# Time: 2019-10-24-11:02 
# Author: dongshichao

'''
给定一个带有头结点 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。

思路：
快满指针
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast,slow = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow