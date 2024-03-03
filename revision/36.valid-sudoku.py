#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col,row,box= collections.defaultdict(set),collections.defaultdict(set),collections.defaultdict(set)
        for r in range(0,9):
            for c in range(0,9):
                curr = board[r][c]
                if curr == ".":
                    continue
                if curr in row[r] or curr in col[c] or curr in box[r//3,c//3] :
                    return False
                row[r].add(curr)
                col[c].add(curr)
                box[r//3,c//3].add(curr)
        return True
                
        
# @lc code=end

