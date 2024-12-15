from typing import List
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for p, t in classes:
            # 증가량을 음수로 저장 (heapq는 최소 힙이므로 음수로 최대 힙처럼 사용)
            heapq.heappush(heap, (-(p + 1) / (t + 1) + p / t, p, t))

        # 추가 학생 배정
        for _ in range(extraStudents):
            increase, p, t = heapq.heappop(heap)  # 증가량이 가장 큰 클래스 선택
            p, t = p + 1, t + 1  # 학생 1명 추가
            heapq.heappush(heap, (-(p + 1) / (t + 1) + p / t, p, t))  # 업데이트된 값 삽입

        # 최종 평균 계산
        return sum(p / t for _, p, t in heap) / len(classes)
