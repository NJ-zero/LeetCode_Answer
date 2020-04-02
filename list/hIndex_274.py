# coding=utf-8 
# @Time    : 2020/4/2 8:27 下午
# @Author  : 'Shichao-Dong'

'''
274.H 指数
给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。编写一个方法，计算出研究者的 h 指数。

h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）至多有 h 篇论文分别被引用了至少 h 次。（其余的 N - h 篇论文每篇被引用次数 不超过 h 次。）

例如：某人的 h 指数是 20，这表示他已发表的论文中，每篇被引用了至少 20 次的论文总共有 20 篇。

 
示例：

输入：citations = [3,0,6,1,5]
输出：3
解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
     由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/h-index
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

         i      0      1       2     3      4       5       6      7
    引用次数     10     9       5     4      3       3       2      0
citations[i]>i  T      T       T     T      F       F       F      F

所以res = 4

'''

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse = True)
        res = 0
        for i in range(len(citations)):
            if citations[i] < res or citations[i] == 0:
                break
            if res== 0 and citations[i] >= res:
                res +=1
            elif res!= 0 and citations[i] > res:  # 考虑到  【1，1，1】 这种情况
                res +=1
        return res