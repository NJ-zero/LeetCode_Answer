# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/2/27 
'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
输入: "()[]{}"
输出: true
输入: "{[]}"
输出: true
输入: "([)]"
输出: false
'''
class Solution(object):
    def isValid(self, s):
        all={'{':'}','[':']','(':')'}
        l=[]
        for i in s:
            if i in all:
                l.append(i)
            else:
                if i==all[l[-1]]:
                    l.pop()
        return l==[]

if __name__=='__main__':
    s=Solution()
    ss='[]{}()[{}](())[{()}]'
    print(s.isValid(ss))