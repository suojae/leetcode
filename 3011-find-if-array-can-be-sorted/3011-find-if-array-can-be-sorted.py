from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)

        # 각 숫자의 '1' 개수를 계산하여 리스트에 저장
        one_counts = [bin(num).count('1') for num in nums]
        
        # 인접한 요소들을 비교하여 교환 가능한지 확인
        for i in range(n):
            for j in range(n - 1):
                if nums[j] > nums[j + 1]:
                    if one_counts[j] == one_counts[j + 1]:
                        # '1'의 개수가 같으면 교환
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]
                        one_counts[j], one_counts[j + 1] = one_counts[j + 1], one_counts[j]
                    else:
                        # '1'의 개수가 다르면 교환 불가
                        continue

        # 정렬된 결과와 원본을 비교하여 확인
        return nums == sorted(nums)


# 모범답안
class Solution2:
    def canSortArray(self, nums):
        num_of_set_bits = bin(nums[0]).count("1")
        max_of_segment = nums[0]
        min_of_segment = nums[0]

        max_of_prev_segment = float("-inf")

        for i in range(1, len(nums)):
            if bin(nums[i]).count("1") == num_of_set_bits:
                max_of_segment = max(max_of_segment, nums[i])
                min_of_segment = min(min_of_segment, nums[i])
            else:  
                if min_of_segment < max_of_prev_segment:
                    return False

                max_of_prev_segment = max_of_segment
                max_of_segment = nums[i]
                min_of_segment = nums[i]
                num_of_set_bits = bin(nums[i]).count("1")

        if min_of_segment < max_of_prev_segment:
            return False

        return True