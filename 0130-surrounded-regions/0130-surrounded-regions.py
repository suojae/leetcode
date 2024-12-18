from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return  # 빈 보드는 처리할 필요가 없음
        
        rows, cols = len(board), len(board[0])
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        # DFS 함수 정의
        def dfs(x, y):
            if x < 0 or x >= rows or y < 0 or y >= cols or board[x][y] != 'O':
                return
            board[x][y] = 'T'  # 'O'를 'T'로 바꿔서 방문 처리
            for i in range(4):  # 상하좌우 탐색
                dfs(x + dx[i], y + dy[i])

        # 1. 가장자리의 'O'를 탐색하여 DFS 실행
        for i in range(rows):
            for j in [0, cols - 1]:  # 첫 번째와 마지막 열
                if board[i][j] == 'O':
                    dfs(i, j)

        for j in range(cols):
            for i in [0, rows - 1]:  # 첫 번째와 마지막 행
                if board[i][j] == 'O':
                    dfs(i, j)

        # 2. 내부를 순회하며 'O'를 'X'로, 'T'를 'O'로 변경
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'  # 둘러싸인 'O'를 'X'로 변환
                elif board[i][j] == 'T':
                    board[i][j] = 'O'  # 방문했던 'T'를 'O'로 복원
