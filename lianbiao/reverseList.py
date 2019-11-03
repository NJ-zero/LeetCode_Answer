# coding=utf-8
# Time: 2019-10-22-17:11 
# Author: dongshichao
'''
反转链表

思路：
很经典的问题，首先设置pre,cur,lat三个指针

pre   cur  lat
null   1 -> 2 -> 3 -> 4 -> 5 -> null
1
2
接着cur.next = pre

pre   cur  lat
null <-1    2 -> 3 -> 4 -> 5 -> null
1
2
接着pre = cur，cur = lat，lat = lat.next

      pre  cur  lat
null <-1    2 -> 3 -> 4 -> 5 -> null
1
2
重复上述操作直到lat=None。

                     pre  cur  lat
null <-1 <- 2 <- 3 <- 4    5 -> null
1
2
最后cur.next = pre即可。

'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        cur = head
        pre = None
        while cur:
            lat = cur.next
            cur.next = pre
            pre = cur
            cur = lat

        return pre
