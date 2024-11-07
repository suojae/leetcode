import itertools
from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        candidates_count = len(candidates)
        result_array = []

        for r in range(1, candidates_count + 1):
            combination_array = itertools.combinations(candidates, r)
            for num_array in combination_array:
                temp_result = 255  # 8비트의 모든 비트가 1인 값
                for num in num_array:
                    temp_result &= num
                result_array.append(temp_result)

        return max(result_array)
