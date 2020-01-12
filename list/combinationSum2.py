# coding=utf-8
# Time: 2019-11-19-19:41 
# Author: dongshichao


'''
40. 组合总和 II

给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

思路：
和 上一个不用，这个是做加法
且 没有强调 没有重复元素 ,且只能使用一次

'''

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        if min(candidates) > target:
            return []
        candidates.sort()
        n = len(candidates)
        res=[]

        def help(i,tar,tmp):
            if tar == target:
                res.append(tmp)
            for j in range(i,n):
                if tar + candidates[j] > target:
                    break
                if j>i and candidates[j] == candidates[j-1]:
                    continue
                help(j+1,tar+candidates[j],tmp+[candidates[j]])
        help(0,0,[])

        return res

    def commm(self, candidates, target):
        if not candidates:
            return []
        if min(candidates) > target:
            return []
        candidates.sort()
        n = len(candidates)
        res=[]

        def help(can,tar,tmp):
            if tar == 0:
                res.append(tmp)
            if tar < 0 :
                return

            for i in range(n):
                if can[i] > target:
                    break
                if i > 0 and can[i] == can[i-1]:
                    continue
                help(can[i+1:],tar - can[i],tmp + [can[i]])

        help(candidates,target,[])
        return res

s=Solution()
print(s.combinationSum2([10,1,2,7,6,1,5],8))
print(s.commm([10,1,2,7,6,1,5],8))