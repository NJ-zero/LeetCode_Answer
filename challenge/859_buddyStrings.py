# coding=utf-8 
# @Time    : 2020/3/25 8:04 下午
# @Author  : 'Shichao-Dong'

'''
859. 亲密字符串
给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false 。
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

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/buddy-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路：
长度不一致 False
相同的字符数 不为0 或 2 False
为0：A 必须有重复
为2：交换后 一样
'''

class Solution(object):
    def buddyStrings(self, A, B):
        if len(A) != len(B):
            return False
        if A == B:
            list_A=[]
            for i in A:
                list_A.append(i)
            if len(A) != len(set(list_A)):
                return True
            else:
                return False

        s = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                s +=1
        if s != 2:
            return False
        else:
            x,y = 0,0
            for i in range(len(A)):
                if A[i] != B[i]:
                    x = i
                    print(x)
                    break
            for j in range(len(A))[::-1]:
                if A[j] != B[j]:
                    y = j
                    print(y)
                    break


            return A[x] == B[y] and A[y]==B[x]



s = Solution()
print(s.buddyStrings("aab","aba"))




