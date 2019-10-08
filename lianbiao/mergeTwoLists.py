# coding=utf-8
# Time: 2019-10-08-19:56 
# Author: dongshichao


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        h = ListNode(-1)
        cur = h

        cur1 = l1
        cur2 = l2

        while cur1 != None and cur2 != None:
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next

        if cur1 != None:
            cur.next = cur1

        if cur2 != None:
            cur.next = cur2
        return h.next

