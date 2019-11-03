# coding=utf-8
# Time: 2019-10-22-19:27 
# Author: dongshichao

'''
相交链表

思路：
求相交结点的方法是，求出链表长度的差值，
长链表的指针先想后移动lenA-lenB。
然后两个链表一起往后走，若结点相同则第一个相交点
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headB or not headA:
            return None

        #求链表长度
        p1 = headA
        p2 = headB
        lenA,lenB = 0,0
        while p1.next:
            lenA +=1
            p1 = p1.next
        while p2.next:
            lenB +=1
            p2 = p2.next

        #将链表指针移动到指定位置
        p1 = headA
        p2 = headB
        if lenA > lenB:
            for i in range(0, lenA - lenB):
                p1 = p1.next
        elif lenA < lenB:
            for i in range(0, lenB - lenA):
                p2 = p2.next
        else:
            pass

        #判断重合位置
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        if p1 ==p2:
            return p1
        else:
            return None



