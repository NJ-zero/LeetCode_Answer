# coding=utf-8
# Time: 2019-11-19-15:13 
# Author: dongshichao

'''
39. 组合总和
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]


划重点：
无重复元素，可以无限制重复选取

思路：同
subset
subsetwithDup
用回溯法

'''

class Solution(object):
    def combinationSum(self, candidates, target):
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
        res=[]

        def help(cand,tar,tmp_list):
            if tar == 0 :
                res.append(tmp_list)
            if tar < 0 :
                return
            for i in range(len(cand)):
                if cand[i] > target:
                    break
                help(cand[i:],tar-cand[i],tmp_list+[cand[i]])

        help(candidates,target,[])
        return res

s=Solution()
print(s.combinationSum([2,3,6,7],8))
