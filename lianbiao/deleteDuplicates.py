# coding=utf-8
# Time: 2019-10-09-14:22 
# Author: dongshichao

'''
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        cur = head
        while cur.next :
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur=cur.next
        return head