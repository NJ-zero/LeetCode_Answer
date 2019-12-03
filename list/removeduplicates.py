# coding=utf-8
# author='Shichao-Dong'
# create time: 2018/8/22 

'''
26. 删除排序数组中的重复项
给定一个排序数组，你需要在[原地]删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在[原地]修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。

如 [0,0,1,1,1,2,2,3,3,4] 返回 [0,1,2,3,4]

解题思路：
注意核心 排序数组，该数组是有序的，所有只需要比较相邻位置的元素，删掉相同的一个即可

2:
双指针 j 来探索 ，i 用来保持 <=i 的元素都不重复
'''
class solution():
    def removeduplicate(self,A):
        i=0
        while i < len(A)-1:
            if A[i] == A[i+1]:
                del(A[i])
                continue
            i+=1
        return A

    def rerr(self,nums):
        if not nums:
            return 0
        i=0
        for j in range(1,len(nums)):
            # 如果i，j 不相等， i+1 ，并将j 的元素指向 i
            if nums[j] != nums[i]:
                i+=1
                nums[i] = nums[j]
        return i+1

if __name__=='__main__':
    s=solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    a=s.removeduplicate(nums)
    print(a)

