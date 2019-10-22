# coding=utf-8
# Time: 2019-10-22-17:33 
# Author: dongshichao

'''
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        l=[]
        p = head
        while p.next:
            l.append(p.val)
            p = p.next
        l.append(p.val)
        return l==l[::-1]




