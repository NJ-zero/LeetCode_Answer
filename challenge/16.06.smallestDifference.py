# coding=utf-8 
# @Time    : 2020/4/14 5:53 下午
# @Author  : 'Shichao-Dong'
'''
给定两个整数数组a和b，计算具有最小差绝对值的一对数值（每个数组中取一个值），并返回该对数值的差

示例：

输入：{1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
输出： 3，即数值对(11, 8)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-difference-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路：
双指针
'''

class Solution(object):
    def smallestDifference(self, a, b):
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: int
        """
        a.sort()
        b.sort()
        minres = abs(a[0] - b[0])
        i,j=0,0
        while i < len(a) and j < len(b):
            minres = min(minres,abs(a[i]-b[j]))
            if a[i] < b[j]:
                i+=1
            else:
                j+=1

        return minres