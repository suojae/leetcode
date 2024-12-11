from bisect import bisect_left
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []  # 증가하는 부분 수열을 저장
        
        for num in nums:
            pos = bisect_left(sub, num)  # 현재 숫자가 들어갈 위치 탐색
            if pos == len(sub):
                sub.append(num)  # 새 숫자를 추가
            else:
                sub[pos] = num  # 기존 숫자를 대체하여 최소화
            
        return len(sub)  # 최장 증가 부분 수열의 길이 반환
