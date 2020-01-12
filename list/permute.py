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

思路四：
见最后一种方法
依次取出数组中的每一个元素，对剩余n-1个元素做全排列，再将该元素与所有全排列组合


'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
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

    def permutepp(self,nums):
        '''
        暂时看不懂 这种解法
        :param nums:
        :return:
        '''
        if not nums:
            return
        res=[]
        n=len(nums)
        vistied = [0] * n
        def help(tmp,length):
            if length == n:
                res.append(tmp)
            for i in range(n):
                if vistied[i]:
                    continue
                vistied[i]=1
                help(tmp+[nums[i]],length+1)
                vistied[i]=0

        help([],0)
        return res


    def pppp(self,nums):
        '''
        例如：[1, 2, 3, 4] 的全排列可以由下面 4 种情况得到：
        1 + permute([2, 3, 4])
        2 + permute([1, 3, 4])
        3 + permute([1, 2, 4])
        4 + permute([1, 2, 3])
        根据这个思路，编码如下，注意：在递归方法执行以后，需要再执行一次交换操作，这一步是状态重置的操作

        :param nums:
        :return:
        '''

        def backtrace(first = 0):
            if first == n:
                out.append(nums[:])
            for i in range(first,n):
                nums[first],nums[i] = nums[i],nums[first]
                backtrace(first + 1)
                nums[first],nums[i] = nums[i],nums[first]

        n = len(nums)
        out = []
        backtrace()
        return out

    def per(self,nums):
        # 依次取出数组中的每一个元素，对剩余n-1个元素做全排列，再将该元素与所有全排列组合
        def helper(nums):
            if len(nums) <=1:
                return [nums]
            n = []
            for i in range(len(nums)):
                iterm = nums.pop(i)
                subres = helper(nums)
                for res in subres:
                    n.append([iterm] + res)
                nums.insert(i,iterm)
            return n

        res = helper(nums)
        return res


s=Solution()
print(s.permute([1,2,3]))
print(s.pppp([1,2,3]))
print(s.per([1,2,3]))
