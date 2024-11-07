import itertools
from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        candidates_count = len(candidates)
        max_count = 0

        for i in range(24, -1, -1):  
            count = 0
            for num in candidates:
                if num & (1 << i):  
                    count += 1
            max_count = max(max_count, count)

        return max_count
