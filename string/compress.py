# coding=utf-8
# Time: 2019-10-17-19:58 
# Author: dongshichao

'''
示例 1：

输入：
["a","a","b","b","c","c","c"]
输出：
返回6，输入数组的前6个字符应该是：["a","2","b","2","c","3"]

说明：
"aa"被"a2"替代。"bb"被"b2"替代。"ccc"被"c3"替代。
示例 2：

输入：
["a"]
输出：
返回1，输入数组的前1个字符应该是：["a"]

示例 3：
输入：
["a","b","b","b","b","b","b","b","b","b","b","b","b"]
输出：
返回4，输入数组的前4个字符应该是：["a","b","1","2"]。

思路：
新建字符串 str_r 用来存在字符和重复的次数
遍历字符串，碰到连续的字符，计算连续次数，如果连续次数大于1 则写入 字母+次数，如果等于1 则只需要写入 字母
'''

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 1:
            return 1
        str_r=""
        count=1
        for i in range(1,len(chars)):
            if chars[i-1] == chars[i]:
                count +=1
            else:
                if count >1 :
                    str_r += chars[i-1] + str(count)
                else:
                    str_r += chars[i-1]
                count = 1
        if count >1:                      #这边主要是计算最后两位及多位相同
            str_r += chars[-1] + str(count)
        else:
            str_r += chars[-1]
        print(str_r)
        strr = list(str_r)
        chars[::] = strr[::]
        return len(strr)

s=Solution()
print(s.compress(["a","a","b","b","c","c"]))