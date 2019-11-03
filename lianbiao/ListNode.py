# coding=utf-8
# Time: 2019-10-24-11:54 
# Author: dongshichao
'''
链表的常见操作

'''

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

    def create_linked_list(self,nums):
        '''
        创建链表
        :param nums:
        :return: 返回创建好的链表头节点，可以得到整个链表的信息
        '''
        if not nums:
            return
        head = pre = ListNode(0)
        for i in nums:
            h = ListNode(i)
            pre.next = h          #挂在已经创建好的链表末尾
            pre = pre.next        #指针后移
        return head

    def copy_linked_list(self,head):
        '''
        拷贝链表，且不改变原来链表的结构
        :param head:
        :return:
        '''
        h = ListNode(0)   #新的节点
        cur = head         #原来的链表挂在新的节点上
        pre = h           #临时链表
        while cur:
            tmp = ListNode(cur.val)    #原链表当前节点构造新的当前节点
            pre.next = tmp           #新节点挂在临时链表上
            cur = cur.next          #当前节点后移
            pre = pre.next          #临时链表后移
        return h.next              #返回新链表

    def print_linked_list(self,head):
        '''
        打印链表
        :param head:
        :return:
        '''
        tmp = head
        nums = []
        while tmp:
            nums.append(tmp.val)
            tmp = tmp.next
        print(nums)
        return nums

    def list_equal(self,head1,head2):
        '''
        判断两个链表是否相等
        :param head1:
        :param head2:
        :return:
        '''
        cur1,cur2=head1,head2    # 不改变输入，使用临时变量
        tmp = head1              # 用于判断环形链表
        while cur1 and cur2:
            if cur1.val != cur2.val:
                return False
            cur1,cur2=cur1.next,cur2.next
            if cur1 == tmp:
                return True
        return not cur1 and not cur2

    def is_circle(self,head):
        '''
        判断链表是否是环形链表
        :param head:
        :return:
        '''
        if not head:
            return False
        tmp = head

        while head:
            head = head.next
            if not head:
                return False
            if head == tmp:
                return True









