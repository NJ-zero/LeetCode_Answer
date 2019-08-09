# coding=utf-8
# Time: 2019-08-09-11:06 
# Author: dongshichao
'''
https://leetcode-cn.com/explore/orignial/card/all-about-array/230/define-with-good-care/
'''

nums = [2,1,0,0,1,0,0,34]

def move (nums):
    i=0
    while i < (len(nums)):
        if nums[i] != 0 :
            i +=1
        else:
            nums.append(nums.pop(i))
        if i >= len(nums)-nums.count(0):
            break
    return nums

print(move(nums))


def move2(nums):
    if len(nums) <= 1:
        return nums
    index = 0
    for i in range(len(nums)):
        if nums[i] !=0:
            nums[index] = nums[i]
            index += 1
    for i in range(index,len(nums)):
        nums[i] = 0
    return nums

print(move2(nums))


nums= [3,2,2,3,4,3,7,89,7,32]
def remove(nums,k):
    n = len(nums)
    if n == 0 :
        return n
    i = 0
    while i < len(nums):
        if nums[i] == k :
            del(nums[i])
            continue
        i+=1
    return len(nums)

def remove2(nums,k):
    i = 0
    index = 0
    while i < len(nums):
        if nums[i] !=k:
            nums[index] = nums[i]
            index += 1
        i +=1
    return index,nums

print(remove(nums,3))
print(remove2(nums,3))

def removedup(nums):
    i=0
    while i < len(nums)-1:
        if nums[i] in nums[i+1:]:
            del(nums[i])
            continue
        i+=1

    return nums

def removedup2(nums):
    n = len(nums)
    if n <= 1:
        return n
    i = 0
    while i < len(nums) - 1:
        if nums[i + 1:].count(nums[i])>1:
            del (nums[i])
            continue
        i += 1
    return nums


nums= [3,2,2,3,4,3,7,89,7,32]
print(removedup2(nums))


def sortcolors(nums):
    pos={0:0,1:0,2:0}
    for i in nums:
        if i in pos:
            pos[i] += 1
        else:
            pos[i] = 1

    for i in range(len(nums)):
        if i < pos[0]:
            nums[i] = 0
        elif i < pos[0]+pos[1]:
            nums[i] = 1
        else:
            nums[i] = 2
    return nums


nums= [1,2,0,0,1,0,2,0,1,1,2]
print(sortcolors(nums))
