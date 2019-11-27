# coding=utf-8
# Time: 2019-11-27-16:37 
# Author: dongshichao

'''
739. 每日温度
根据每日 气温 列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高超过该日的天数。
如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

题目意思
找到比 i 大的数 j, 两个数之间的距离
'''

class Solution(object):
    def dailyTemperatures(self, T):
        """
        正确，但是会超时
        :type T: List[int]
        :rtype: List[int]
        """
        if not T :
            return []
        n = len(T)
        if n <=1:
            return [0]
        L = [ 0 for i in T]
        for i in range(n-1):
            for j in range(i,n):
                if T[j]>T[i]:
                    L[i] = j-i
                    break
        return L

    def dailystack(self, T):
        ans = [0] * len(T)
        stack = []
        for i in range(len(T)-1,-1,-1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans

s=Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
for i in range(5,-1,-1):
    print(i)

print(s.dailystack([73, 74, 75, 71, 69, 72, 76, 73]))