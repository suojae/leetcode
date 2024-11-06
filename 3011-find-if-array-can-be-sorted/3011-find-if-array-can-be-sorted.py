from typing import List
from collections import defaultdict

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # 이미 정렬된 경우 True 반환
        if nums == sorted(nums):
            return True

        groups = defaultdict(list)
        for num in nums:
            count = bin(num).count('1')  # 이진수에서 '1'의 개수를 세기
            groups[count].append(num)

        sorted_nums = []
        for count in sorted(groups.keys()):
            sorted_nums.extend(sorted(groups[count]))

        return sorted_nums == sorted(nums)
