class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
    
        left_sum = 0
        right_sum = sum(nums)
        count = 0
        array_length = len(nums)

        for index in range(array_length-1):
            left_sum+=nums[index]
            right_sum-=nums[index]

            if left_sum>=right_sum:
                count+=1
            
        return count
            

            
            
            