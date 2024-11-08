from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:

        max_k = (1 << maximumBit) - 1
        
        xor_result = 0
        for num in nums:
            xor_result ^= num
        
        answer_array = []

        for i in range(len(nums)):
            k = max_k  
            answer_array.append(xor_result ^ k)  
            xor_result ^= nums[-1]  
            nums.pop()  

        return answer_array
