#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        box = collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".": continue
                if (num in row[i] or
                   num in col[j] or
                   num in box[(i//3,j//3)]):
                   print(num)
                   return False 
                else :
                    row[i].add(num)
                    col[j].add(num)
                    box[(i//3,j//3)].add(num)
        return True
# @lc code=end

