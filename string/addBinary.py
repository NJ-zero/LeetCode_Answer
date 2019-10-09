# coding=utf-8
# Time: 2019-10-09-11:27 
# Author: dongshichao

'''
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"

思路：
将a,b 反转后存入数组中
然后将两个数组同位置的数相加，相加的结果存在另一个数组s中
如果s最后一位 0 ，则去掉
将3翻转后，合并成 字符串
'''

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a=a[::-1]
        b=b[::-1]
        l = max(len(a),len(b))
        s= [ 0 for _ in range(l+1)]
        sa=[ 0 for _ in range(l)]
        sb=[ 0 for _ in range(l)]

        for i in range(len(a)):
            sa[i]=int(a[i])
        for j in range(len(b)):
            sb[j]=int(b[j])

        for i in range(l):
            if sa[i]+sb[i]+s[i] < 2:         #关键在这边
                s[i]=sa[i]+sb[i]+s[i]
            else:
                s[i]=(sa[i]+sb[i]+s[i])%2     #这边也需要注意
                s[i+1]=1

        if s[-1]==0:
            res=s[:-1]
            res=[str(i) for i in res]
            return "".join(res[::-1])
        else:
            s=[str(i) for i in s]
            return "".join(s[::-1])

if __name__ == "__main__":
    s=Solution()

    print(s.addBinary("1010","1011"))