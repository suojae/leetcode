from typing import List

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:

        def is_prime(num: int) -> bool:
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1): 
                if num % i == 0:
                    return False
            return True
        
        def find_peak_prime(num: int, prev: int) -> int:
            for i in range(num - 1, 1, -1):
                if is_prime(i) and num - i > prev:
                    return i
            return 0

        prev = 0
        for num in nums:
            p = find_peak_prime(num, prev)
            if num - p <= prev:
                return False
            prev = num - p  

        return True
