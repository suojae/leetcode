from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        check_duplicate = {}  # 딕셔너리로 중복 여부 체크
        unique_index = 0  # 고유한 요소를 저장할 위치를 가리킵니다.
        
        for i in range(len(nums)):
            if nums[i] not in check_duplicate:  # 중복이 아닌 경우
                check_duplicate[nums[i]] = True  # 중복 체크 딕셔너리에 추가
                nums[unique_index] = nums[i]  # 고유 요소를 앞부분에 배치
                unique_index += 1  # 고유 요소 위치를 한 칸 이동

        return unique_index  # 고유한 요소의 개수를 반환
