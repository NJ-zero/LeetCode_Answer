# coding=utf-8
# Time: 2019-10-19-16:47 
# Author: dongshichao

'''
给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false 。

示例 1：

输入： A = "ab", B = "ba"
输出： true
示例 2：

输入： A = "ab", B = "ab"
输出： false
示例 3:

输入： A = "aa", B = "aa"
输出： true
示例 4：

输入： A = "aaaaaaabc", B = "aaaaaaacb"
输出： true
示例 5：

输入： A = "", B = "aa"
输出： false

思路：
就三种情况：
字符串长度不相等, 直接返回false
字符串相等的时候, 只要有重复的元素就返回true
A, B字符串有不相等的两个地方, 需要查看它们交换后是否相等即可.
'''


class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        list_A = list(A)
        list_B = list(B)
        if len(A) != len(B) or len(A) <2:
            return False

        if A == B :
            if len(list(set(list_A))) < len(A):
                return True
            else:
                return False
        if A != B:
            count =0
            res=[]
            for i in range(len(A)):
                if list_A[i] != list_B[i]:
                    count += 1
                    res.append(i)
                if count > 2:
                    return False
        list_A[res[0]],list_A[res[1]] = list_A[res[1]],list_A[res[0]]
        return list_A == list_B


    def budd(self,A,B):
        '''
        评论区的方法
        :type A: str
        :type B: str
        :rtype: bool
        '''

        if len(A) != len(B): return False

        if A == B and len(set(A)) < len(A): return True

        dif=[(a,b) for a,b in zip(A,B) if a != b]
        return len(dif[A,B])==2 and dif[0] == dif[1][::-1]

s= Solution()
print(s.buddyStrings("ab","ba"))
print([a+b for a,b in zip("abccc","baccc")])