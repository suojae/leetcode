import heapq
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 두 배열의 총 길이를 계산
        total_length = len(nums1) + len(nums2)
        median_index = total_length // 2  # 중간 인덱스 계산

        # 최소힙으로 변환
        heapq.heapify(nums1)
        heapq.heapify(nums2)
        
        merged = []  # 두 배열에서 중간값까지의 숫자를 저장할 배열
        compare_count = 0

        # 중간값에 도달할 때까지 최소값을 계속 가져옴
        while compare_count <= median_index:
            if not nums1:  # nums1이 비었을 때
                merged.append(heapq.heappop(nums2))
            elif not nums2:  # nums2가 비었을 때
                merged.append(heapq.heappop(nums1))
            else:
                if nums1[0] < nums2[0]:
                    merged.append(heapq.heappop(nums1))
                else:
                    merged.append(heapq.heappop(nums2))
            compare_count += 1
        
        # 총 배열의 길이에 따라 중간값을 계산
        if total_length % 2 == 1:
            return merged[-1]  # 홀수일 경우 마지막 값을 반환
        else:
            return (merged[-1] + merged[-2]) / 2.0  # 짝수일 경우 두 값의 평균을 반환
