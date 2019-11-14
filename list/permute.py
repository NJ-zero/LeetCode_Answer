# coding=utf-8
# Time: 2019-11-14-17:23 
# Author: dongshichao

'''
46. 全排列

给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

思路：
只有两个元素时，只有两种排列 【1，2】【2，1】
tmp=nums[i]  i>=2
加入第三个元素，原排序变为【1，2，3】 【2，1，3】 out.append(tmp)
将最后一个数，分别与前面的数互换
【1，2，3】【3，2，1】【1，3，2】【2，1，3】 【3，1，2】 【2，3，1】

for i in range(len(n)-1):
    s=[k for k in n]
    s[len(s)-1]=s[i]
    s[i]=x

对上面的方法迭代，不断加入新的元素


'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 1:
            return [nums]
        output=[[nums[0],nums[1]],[nums[1],nums[0]]]

        for i in range(2,len(nums)):
            tmp=nums[i]
            output_new=[]
            for j in range(len(output)):
                output[j].append(tmp)
                output_new.append(output[j])
                for k in range(len(output[j])-1):
                    line=[n for n in output[j]]
                    line[len(line)-1] = line[k]
                    line[k]=tmp
                    output_new.append(line)
            output=output_new
        return output

