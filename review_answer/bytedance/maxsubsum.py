# coding=utf-8
# Time: 2020-01-19-16:09 
# Author: dongshichao

'''
最大连续子数组和
'''

def maxsubsum(nums):
    n = len(nums)
    dp = [0] * n
    dp[0] = max(nums[0],0)
    for i in range(1,n):
        dp[i] = max(dp[i-1]+nums[i],nums[i])

    return max(dp)

print(maxsubsum([-2,1,-3,4,-1,2,1,-5,4]))


'''
最长无重复子数组
'''
def maxlength(s):
    i,j=0,0
    res = 0
    while i < len(s):
        if j < len(s) and s[j] not in s[i:j]:
            j+=1
            res = max(res,j-i)
        else:
            i+=1
    return res