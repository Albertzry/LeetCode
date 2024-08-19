class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def backtrack(board, i, j):
            m, n = 9, 9
            if j == n:
                # 穷举到最后一列的话就换到下一行重新开始。
                return backtrack(board, i + 1, 0)
            if i == m:
                # 找到一个可行解，触发 base case
                return True

            if board[i][j] != '.':
                # 如果有预设数字，不用我们穷举
                return backtrack(board, i, j + 1)

            for ch in '123456789':
                # 如果遇到不合法的数字，就跳过
                if not isValid(board, i, j, ch):
                    continue

                board[i][j] = ch
                # 如果找到一个可行解，立即结束
                if backtrack(board, i, j + 1):
                    return True
                board[i][j] = '.'
            # 穷举完 1~9，依然没有找到可行解，此路不通
            return False

        def isValid(board, r, c, n):
            for i in range(9):
                # 判断行是否存在重复
                if board[r][i] == n: return False
                # 判断列是否存在重复
                if board[i][c] == n: return False
                # 判断 3 x 3 方框是否存在重复
                if board[(r // 3) * 3 + i // 3][(c // 3) * 3 + i % 3] == n:
                    return False
            return True

        backtrack(board, 0, 0)

            