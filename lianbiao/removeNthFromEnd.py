# coding=utf-8
# Time: 2019-10-21-20:08 
# Author: dongshichao


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        h= ListNode(0)        #定一个临时节点
        h.next = head         #将链表挂在临时节点上，临时节点成为了头节点
        p,q= h,h              # 快慢指针开始位置都是临时节点

        for i in range(n):     #快指针提前走n步
            p = p.next

        while p.next:           #快满指针同时走，直到快指针到末尾
            p = p.next
            q= q.next

        q.next = q.next.next     #把满指针的下一节点删除

        return h.next