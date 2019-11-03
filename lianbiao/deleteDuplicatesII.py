# coding=utf-8
# Time: 2019-10-22-11:44 
# Author: dongshichao

'''
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3


'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = ListNode(0)
        h.next = head

        pre,cur = h,head

        while cur != None:
            dup=False
            while cur.next != None and cur.val == cur.next.val:
                cur = cur.next
                dup = True
            if dup == False:
                pre = cur
            else:
                pre.next=cur.next

            cur = cur.next

        return h.next
