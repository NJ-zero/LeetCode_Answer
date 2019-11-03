# coding=utf-8
# author='Shichao-Dong'
# create time: 2018/8/23
'''
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
如果不存在最后一个单词，请返回 0 。
输入: "Hello World"
输出: 5
"   a  "
1
'''

class solution():
    def lengthOfLastWord(self,s):
        return (len(s.strip().split(" ")[-1]))

if __name__=="__main__":
    s=solution()
    ss=" hello wolrd asj  "
    a=s.lengthOfLastWord(ss)
    print(a)