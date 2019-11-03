# coding=utf-8
# Time: 2019-10-31-17:50 
# Author: dongshichao

'''
744.寻找比目标字母大的最小字母

给定一个只包含小写字母的有序数组letters 和一个目标字母 target，寻找有序数组里面比目标字母大的最小字母。

数组里字母的顺序是循环的。举个例子，如果目标字母target = 'z' 并且有序数组为 letters = ['a', 'b']，则答案返回 'a'。

示例:

输入:
letters = ["c", "f", "j"]
target = "a"
输出: "c"

输入:
letters = ["c", "f", "j"]
target = "c"
输出: "f"

输入:
letters = ["c", "f", "j"]
target = "j"
输出: "c"

输入:
letters = ["c", "f", "j"]
target = "k"
输出: "c"


'''

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        n = len(letters)
        i ,j = 0,n-1

        if target >= letters[-1] or target < letters[0]:
            return letters[0]

        while i <= j:
            mid = i + (j-i)//2
            if letters[mid] <= target:
                i = mid + 1
            else:
                j = mid - 1

        return letters[i]



s=Solution()
print(s.nextGreatestLetter(["c","f","j"],"c"))


