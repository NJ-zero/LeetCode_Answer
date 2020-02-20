# coding=utf-8
# Time: 2020-01-15-15:56 
# Author: dongshichao

'''
100W 个数中 找 前 100 个
'''

import random

# 这边简单处理，1000 个 找前 10 个
lists = random.sample(range(3000000),1000)
print(lists)
print(sorted(lists,reverse=True))

s={}
for i in range(10):
    s[i] = float("-inf")

for num in lists:
    s = dict(sorted(s.items(),key=lambda x : x[1]))
    for i in s:
        if s[i] < num:
            s[i] = num
            break

print(list(s.values()))

ss= lambda x,y:x+y
print(ss(2,3))