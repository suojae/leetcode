from itertools import combinations

class Solution:
    def countMaxOrSubsets(self, nums):
        max_or = 0
        count = 0

        for num in nums:
            max_or |= num 

        def bitwise_or(subset):
            result = 0
            for num in subset:
                result |= num
            return result

        n = len(nums)

        for r in range(1, n + 1):
            for subset in combinations(nums, r):
                if bitwise_or(subset) == max_or:
                    count += 1

        return count 

