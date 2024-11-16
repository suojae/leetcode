class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans_arr = []
        
        for start in range(len(nums) - k + 1):  
            tmp_arr = nums[start:start + k]    #
            
            
            if all(tmp_arr[i] + 1 == tmp_arr[i + 1] for i in range(len(tmp_arr) - 1)):
                ans_arr.append(max(tmp_arr))  # 연속적이면 최댓값 추가
            else:
                ans_arr.append(-1)           # 연속적이지 않으면 -1 추가
                
        return ans_arr
