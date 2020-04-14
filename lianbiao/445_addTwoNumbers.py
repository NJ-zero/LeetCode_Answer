# coding=utf-8 
# @Time    : 2020/4/14 4:39 下午
# @Author  : 'Shichao-Dong'

'''
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。

 
进阶：

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

 
示例：

输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路
遇到逆向的，想到栈
'''
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1,s2=[],[]
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.val
        head = ListNode(0)
        flag = 0
        while s1 or s2 or flag != 0:
            if not s1:
                a = 0
            else:
                a = s1.pop()
            b = 0 if not s2 else s2.pop()

            cur = a+b+flag
            flag = cur // 10
            cur = cur % 10
            curnode = ListNode(cur)
            curnode.next = head.next
            head.next = curnode
        return head.next