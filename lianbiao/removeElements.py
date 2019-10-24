# coding=utf-8
# Time: 2019-10-24-11:11 
# Author: dongshichao

'''
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        h = ListNode(0)
        h.next = head    #定义一个临时节点，并把输入链表挂在上面
        cur = h

        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next     #下一个节点值要删除则删除
            else:
                cur = cur.next               #否则节点后移
        return h.next                        #返回处理后的节点