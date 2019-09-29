# coding=utf-8
# author='Shichao-Dong'
# create time: 2018/8/22 

'''
移除列表中重复的元素
给定一个排序数组，你需要在[原地]删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在[原地]修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。

如 [0,0,1,1,1,2,2,3,3,4] 返回 [0,1,2,3,4]
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


if __name__=='__main__':
    s=solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    a=s.removeduplicate(nums)
    print(a)

