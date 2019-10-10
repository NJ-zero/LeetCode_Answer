# coding=utf-8
# Time: 2019-10-10-10:27 
# Author: dongshichao

'''
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]


'''


class Solution(object):
    def getRow(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res=[[1]]
        if numRows == 0 :
            return [1]
        else:
            for i in range(1,numRows+1):
                n = [ 1 for _ in range(i+1)]
                for j in range(1,i):
                    n[j] = res[i-1][j] + res[i-1][j-1]
                res.append(n)

        return res[-1]

if __name__ == "__main__":
    s = Solution()
    print(s.getRow(1))