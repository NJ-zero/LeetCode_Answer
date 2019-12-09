# coding=utf-8
# Time: 2019-12-09-17:04 
# Author: dongshichao

'''
22.括号生成

给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]


思路一：
i=n 的排列等于
"(" + 【i=p时所有括号的排列组合】 + ")" + 【i=q时所有括号的排列组合】
其中 p + q = n-1，且 p q 均为非负整数。

思路二：
回溯法，但是还没看懂！！！！！
如果我们还剩一个位置，我们可以开始放一个左括号。
如果它不超过左括号的数量，我们可以放一个右括号

'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        all=[]     # all[i] 表示 i 时的结果
        all.append([None]) # 0 是为空
        all.append(["()"]) # 1 是 （）
        for i in range(2,n+1):    # 开始计算 i 时的情况
            res=[]
            for j in range(i):     # 遍历 p,q ，p+q = i-1
                list_1 = all[j]
                list_2 = all[i-1-j]
                for k1 in list_1:
                    for k2 in list_2:
                        if k1 is None:
                            k1 = ""
                        if k2 is None:
                            k2 = ""

                        l = "(" + k1 + ")" + k2
                        res.append(l)
            all.append(res)
        return all[-1]

    def gggg(self, n):
        res = []

        def dfs(left,right,tmp):
            if left == n and right == n:
                res.append(tmp)
                return

            if left < n:
                dfs(left+1,right,tmp+"(")
            if left > right and right<n:
                dfs(left,right+1,tmp+")")

        dfs(0,0,"")

        return res

s=Solution()
print(s.generateParenthesis(3))