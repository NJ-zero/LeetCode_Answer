# coding=utf-8
# author='Shichao-Dong'
# create time: 2018/8/22 
'''
移除指定元素
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