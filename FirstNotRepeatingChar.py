# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/2/25
'''
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中
找到第一个只出现一次的字符,并返回它的位置,
如果没有则返回 -1（需要区分大小写）.
'''
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        count={}
        for i in s :
            count[i]=1 if i not in count else count[i]+1
        for i in s:
            if count[i]==1:
                return i,s.index(i)
            else:
                pass
        return -1

if __name__=='__main__':
    s=Solution()
    ss="loveabcdfghiabclo"
    i = s.FirstNotRepeatingChar(ss)
    print(i)
