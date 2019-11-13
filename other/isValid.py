# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/2/27 
'''
20.有效的括号
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


解题思路：
每组括号，组成一对 k v
遍历字符串，如果i 在 k中，就加到列表中
如果不在k中，肯定就是v,且这个v 应该和。list最后一个元素相等

理想情况，最终的list为空
'''
class Solution(object):
    def isValid(self, s):
        all = {'{': '}', '[': ']', '(': ')'}
        l = []

        if len(s) % 2 == 1:
            return False
        if len(s) == 0:
            return True
        if s[0] not in all:
            return False
        for i in s:
            if i in all:
                l.append(i)
            else:
                if not l or all[l.pop()] != i:
                    return False
        return l == []

    def isValid2(self, s):
        all = {'{': '}', '[': ']', '(': ')'}
        l = []

        if len(s) % 2 == 1:
            return False
        if len(s) == 0:
            return True
        if s[0] not in all:
            return False
        for i in s:
            if i in all:
                l.append(all[i])
                print(l)
            else:
                if not l or l.pop() != i:
                    return False
        return l == []

if __name__=='__main__':
    s=Solution()
    ss="{}[]([])"
    print(s.isValid(ss))