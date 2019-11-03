# coding=utf-8
# author='Shichao-Dong'
# create time: 2018/8/22 
'''
移除指定元素
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:

给定 nums = [3,2,2,3], val = 3,

函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。


'''

class Solution():

    def removeElement(self,nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        while i < len(nums):
            if nums[i] == val:
                del(nums[i])
                continue
            i+=1
        print (nums)

    def removee(self,nums,val):
        n = len(nums)
        i ,j = 0,0
        while i <n:
            if nums[i] != val:
                nums[j] = nums[i]
                j+=1
            i+=1
        print(nums)

if __name__=='__main__':
    s=Solution()
    nums=[1,2,3,4,5,1,3,7,4,3,2]
    val=2
    s.removeElement(nums,val)
    s.removee(nums,val)