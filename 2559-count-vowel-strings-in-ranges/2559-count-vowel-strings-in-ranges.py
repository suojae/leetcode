from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}

        # 사전 처리: 조건에 맞는 문자열 여부 저장
        is_vowel_word = [
            word[0] in vowels and word[-1] in vowels for word in words
        ]

        # 누적 합 배열 생성
        prefix_sum = [0]
        for value in is_vowel_word:
            prefix_sum.append(prefix_sum[-1] + value)

        # 쿼리 처리
        answer_array = []
        for x, y in queries:
            count = prefix_sum[y + 1] - prefix_sum[x]
            answer_array.append(count)

        return answer_array
