from typing import List
from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        answer = []
        
        # words2 내부 단어들의 문자 빈도 중 최댓값 계산
        max_freq = Counter()
        for word in words2:
            word_count = Counter(word)
            for char, freq in word_count.items():
                max_freq[char] = max(max_freq[char], freq)

        for word1 in words1:
            word_count = Counter(word1)
            count = 0  
            for char, freq in max_freq.items():
                if word_count[char] >= freq:
                    count += 1
            if count == len(max_freq): 
                answer.append(word1)

        return answer
