# coding=utf-8
# Time: 2019-10-09-19:46 
# Author: dongshichao

'''
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]


'''

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res=[[1]]
        if numRows == 0 :
            return []
        if numRows == 1:
            return res
        else:
            for i in range(1,numRows):
                n = [ 1 for _ in range(i+1)]
                for j in range(1,i):
                    n[j] = res[i-1][j] + res[i-1][j-1]
                res.append(n)

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.generate(5))