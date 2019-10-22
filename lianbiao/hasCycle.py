# coding=utf-8
# Time: 2019-10-22-17:06 
# Author: dongshichao

'''
给定一个链表，判断链表中是否有环

思路：
快慢指针
'''



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        fast,slow = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False