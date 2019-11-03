# coding=utf-8
# Time: 2019-10-15-15:28 
# Author: dongshichao

'''
给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

每组都有 X 张牌。
组内所有的牌上都写着相同的整数。
仅当你可选的 X >= 2 时返回 true。

示例 1：

输入：[1,2,3,4,4,3,2,1]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
示例 2：

输入：[1,1,1,2,2,2,3,3]
输出：false
解释：没有满足要求的分组。
示例 3：

输入：[1]
输出：false
解释：没有满足要求的分组。
示例 4：

输入：[1,1]
输出：true
解释：可行的分组是 [1,1]

解题思路：
先求每个元素出现的次数，
再求次数是否存在公约数（最小为2 的公约数），存在即可以
'''

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        dic = {}
        for i in deck:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        res = dic.values()
        if min(res) == 1:
            return False
        ss = []
        for i in range(2,min(res)+1):
            count = 0
            for j in res:
                if j % i !=0:
                    count +=1

            ss.append(count)
        return 0 in ss


s = Solution()
print(s.hasGroupsSizeX([1,1]))