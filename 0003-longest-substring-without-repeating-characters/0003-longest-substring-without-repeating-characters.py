class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # 문자 마지막 위치 저장
        left = 0  # 윈도우의 왼쪽 경계
        max_length = 0  # 최장 길이 저장

        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                # 중복 발생 시 왼쪽 포인터 갱신
                left = char_index[s[right]] + 1

            # 현재 문자 위치 갱신
            char_index[s[right]] = right

            # 최대 길이 갱신
            max_length = max(max_length, right - left + 1)

        return max_length
