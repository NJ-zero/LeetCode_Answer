# coding=utf-8
# author='Shichao-Dong'
# create time: 2018/8/24
'''
给定两个字符串 A 和 B, 寻找重复叠加字符串A的最小次数，使得字符串B成为叠加后的字符串A的子串，如果不存在则返回 -1。
举个例子，A = "abcd"，B = "cdabcdab"。
答案为 3， 因为 A 重复叠加三遍后为 “abcdabcdabcd”，此时 B 是其子串；A 重复叠加两遍后为"abcdabcd"，B 并不是其子串
'''

class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        lenA=len(A)
        lenB=len(B)
        i=lenB // lenA
        if B not in A:
            for n in range(i,2*i+3):
                if B in A * n:
                    return (n)
                    break
            else:
                return -1
        else:
            return 1

if __name__=="__main__":
    s=Solution()
    A='a'
    B="aa"
    a=s.repeatedStringMatch(A,B)
    print(a)