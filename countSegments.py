# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/3/5 
'''
统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符

输入: "Hello, my name is John"
输出: 5
'''

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0
        else:
            str_s=s.strip()
            list_s=str_s.split(" ")
            count=0
            for i in list_s:
                if i !="" and i!=" ":
                    count+=1
            return count

if __name__=='__main__':
    s=Solution()
    a = s.countSegments("      ")
    print(a)
