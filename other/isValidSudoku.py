# coding=utf-8
# Time: 2019-12-10-14:51 
# Author: dongshichao

'''
36. 有效的数独

判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。


'''


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        for i in range(9):
            for j in range(9):
                num=board[i][j]

                if num != '.':
                    num = int(num)
                    box_index = (i//3) * 3 + j//3

                    rows[i][num] = rows[i].get(num,0) + 1
                    columns[j][num] = columns[j].get(num,0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num,0) + 1

                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False

        return True

