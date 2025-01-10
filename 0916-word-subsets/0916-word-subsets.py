from typing import List
from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        answer = []

        # words2의 문자 개수 중 최댓값을 저장
        max_freq = Counter()
        for word2 in words2:
            word_count = Counter(word2)
            for char, freq in word_count.items():
                max_freq[char] = max(max_freq[char], freq)

        for word1 in words1:
            word_count = Counter(word1)
            count = 0  # 조건을 만족하는 개수
            for char, freq in max_freq.items():
                if word_count[char] >= freq:
                    count += 1
            if count == len(max_freq):  # 모든 조건을 만족하는 경우
                answer.append(word1)

        return answer
