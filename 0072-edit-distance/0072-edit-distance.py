class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # DP 테이블 초기화 (m+1 x n+1 크기)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 초기 상태 설정
        for i in range(m + 1):
            dp[i][0] = i  # word2가 빈 문자열인 경우 word1의 문자를 모두 삭제
        for j in range(n + 1):
            dp[0][j] = j  # word1이 빈 문자열인 경우 word2의 문자를 모두 삽입
        
        # DP 계산
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # 같은 문자는 그대로 사용
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],     # 삭제
                        dp[i][j - 1],     # 삽입
                        dp[i - 1][j - 1]  # 교체
                    )
        
        return dp[m][n]
