class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        unique_palindromes = 0
        
        for char in set(s):  # a~z 중 존재하는 문자만 확인
            first = s.find(char)  # 첫 등장 위치
            last = s.rfind(char)  # 마지막 등장 위치
            
            if first < last:  # 최소한 3글자가 되어야 함
                unique_middle_chars = set(s[first + 1:last])  # 중간 문자들 집합
                unique_palindromes += len(unique_middle_chars)  # 가능한 길이 3 회문 개수 추가
        
        return unique_palindromes
