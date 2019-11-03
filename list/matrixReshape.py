# coding=utf-8
# Time: 2019-10-11-11:13 
# Author: dongshichao

'''
如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。

示例 1:

输入:
nums =
[[1,2],[3,4]]
r = 1, c = 4
输出:
[[1,2,3,4]]
解释:
行遍历nums的结果是 [1,2,3,4]。新的矩阵是 1 * 4 矩阵, 用之前的元素值一行一行填充新矩阵。
示例 2:

输入:
nums =
[[1,2],[3,4]]
r = 2, c = 4
输出:
[[1,2],[3,4]]
解释:
没有办法将 2 * 2 矩阵转化为 2 * 4 矩阵。 所以输出原矩阵。


解体思路：
将所有元素装入一个列表中
分成 r 个数组，每个数组 c 个元素
'''

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        res=[]
        for i in nums:
            for j in i :
                res.append(j)
        n= len(res)
        res_num=[]
        if r *c != n:
            return nums
        for i in range(r):
            m=[]
            sum = 0
            while sum < c :
                if res :
                    m.append(res.pop(0))
                sum += 1
            res_num.append(m)
        return res_num

s =Solution()
print(s.matrixReshape([[1,2],[3,4]],2,4))