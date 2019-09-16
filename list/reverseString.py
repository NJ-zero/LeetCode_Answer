# coding=utf-8
# Time: 2019-09-16-19:30 
# Author: dongshichao

'''
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

示例 2：

输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]



思路：
要求使用O（1）的额外空间,遍历整个列表前后交换
'''


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i,j = 0, len(s)-1
        while i<j:
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1

if __name__ == "__main__":
    s = Solution()
    (s.reverseString(['a','b','c','d','e','f']))