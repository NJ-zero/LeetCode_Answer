# coding=utf-8
# Time: 2019-10-10-14:31 
# Author: dongshichao

'''
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:

输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]


'''

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[ i for i in range(1,len(nums)+1)]
        print(res)
        n=[]
        nums = list(set(nums))
        for i in res:
            if i not in nums:
                n.append(i)
        return n
    def finddd(self,nums):

        print(list(set(range(1, len(nums)+1))-set(nums)))


    def findDisapper(self,nums):
        '''
        每个元素的值 v 都小于等于 num长度 n
        用读取到的元素 v ,寻找下标 j = v-1
        如果nums[j] 被访问过，则标为负数 *-1（方便理解新建一个数组res）

        # 剩下的为正的元素的下标，则未访问过，
        # 代表下标 i 对应的值 i+1 为未出现过的元素
        :param nums:
        :return:
        '''
        res = [i for i in range(1, len(nums) + 1)]
        for i ,v in enumerate(nums):
            j= abs(v) - 1
            if nums[j] >0 :
                nums[j] *= -1

            if res[j] > 0 :
                res[j] *= -1

        return [i+1 for i ,v in enumerate(res) if v>0]




s= Solution()
print(s.findDisappearedNumbers([1,1]))
print(s.findDisapper([4,3,2,7,8,2,3,1]))