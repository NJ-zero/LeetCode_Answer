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
        h = ListNode(0)       #创建一个空链表
        cur = h               #创建一个指针指向新的链表头

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next       #依次判断两个旧链表头结点val大小，cur指向小的那个

        if l1 != None:           #一个旧链表全部接到新链表后，将另一个链表剩下的部分接到新链表
            cur.next = l1
        if l2 != None:
            cur.next = l2
        return h.next

    def mergedigui(self, l1, l2):
        if not l1 : return l2
        if not l2 : return l1

        if l1.val < l2.val:
            l1.next = self.mergedigui(l1.next,l2)
            return l1
        else:
            l2.next = self.mergedigui(l1,l2.next)
            return l2



s=Solution()
print(s.mergeTwoLists())
