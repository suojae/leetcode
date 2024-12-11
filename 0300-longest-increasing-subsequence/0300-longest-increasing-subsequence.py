class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [] 

        for num in nums:
            if not res or num > res[-1]: 
                res.append(num)
            else:
                left = 0
                right = len(res) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if res[mid] < num:
                        left = mid + 1
                    else:
                        right = mid - 1
                
                res[left] = num
        
        return len(res)
