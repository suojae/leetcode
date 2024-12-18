from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return 
        
        rows, cols = len(board), len(board[0])
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        def dfs(x, y):
            if x < 0 or x >= rows or y < 0 or y >= cols or board[x][y] != 'O':
                return
            board[x][y] = 'V'  # 'O'를 'T'로 바꿔서 방문 처리
            for i in range(4): 
                dfs(x + dx[i], y + dy[i])

        # 1. 가장자리 'O' 탐색 -> DFS 실행
        for i in range(rows):
            for j in [0, cols - 1]:  # 첫 번째와 마지막 열
                if board[i][j] == 'O':
                    dfs(i, j)

        for j in range(cols):
            for i in [0, rows - 1]:  # 첫 번째와 마지막 행
                if board[i][j] == 'O':
                    dfs(i, j)

        # 2. 내부를 순회하며 'O'를 'X', 'T'를 'O'로 변경
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'  # 둘러싸인 'O'를 'X'로 변환
                elif board[i][j] == 'V':
                    board[i][j] = 'O'  # 방문했던 'T'를 'O'로 복원
