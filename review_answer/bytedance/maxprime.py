# coding=utf-8
# Time: 2020-01-16-14:12 
# Author: dongshichao
'''
不大于n的最大质数
'''

def maxprime(n):
    if n <=3:
        return n
    dp=[1]*n
    for i in range(2,n):
        j=i
        while (i*j < n):
            dp[i*j] =0
            j+=1
    return dp

print(maxprime(5))
dp = maxprime(20)
print(20-1-dp[::-1].index(1))