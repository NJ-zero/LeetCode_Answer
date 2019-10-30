# coding=utf-8
# Time: 2019-10-30-16:20 
# Author: dongshichao

'''
我们正在玩一个猜数字游戏。 游戏规则如下：
我从 1 到 n 选择一个数字。 你需要猜我选择了哪个数字。
每次你猜错了，我会告诉你这个数字是大了还是小了。
你调用一个预先定义好的接口 guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：

-1 : 我的数字比较小
 1 : 我的数字比较大
 0 : 恭喜！你猜对了！

思路：
guess 方法，返回-1 则 最大值为mid-1
返回1 则 最小值为mid+1
'''
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        h = n
        while l <= h:
            mid = (l + h)//2
            if not guess(mid):
                return mid
            elif guess(mid) == -1:
                h = mid-1
            else:
                l = mid +1