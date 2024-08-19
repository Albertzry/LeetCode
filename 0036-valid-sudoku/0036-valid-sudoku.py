class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def judge(my_list):
            num=set()
            for i in range(9):
                if my_list[i]!="." and my_list[i] in num:
                    return False
                else:
                    num.add(my_list[i])
            return True
        column=[]
        grid=[[[],[],[]],[[],[],[]],[[],[],[]]]
        for i in range(9):
            if not judge(board[i]):
                return judge(board[i])
            column.append([])
            for j in range(9):
                column[i].append(board[j][i])
                grid[i//3][j//3].append(board[i][j])
        for i in range(9):
            if not judge(column[i]):
                return judge(column[i])
        for i in range(3):
            for j in range(3):
                if not judge(grid[i][j]):
                    return judge(grid[i][j])
        return True