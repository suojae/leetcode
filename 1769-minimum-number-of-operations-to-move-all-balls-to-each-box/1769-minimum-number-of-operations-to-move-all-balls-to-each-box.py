from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        def recur(index: int, output: List[int]) -> List[int]:
            if index == len(boxes):  # Base case: 모든 박스를 처리하면 결과 반환
                return output

            total = 0
            for j in range(len(boxes)):  # 모든 공의 위치를 탐색
                if boxes[j] == '1':  # 공이 있는 경우만 이동 거리 누적
                    total += abs(index - j)

            output.append(total)  # 결과 저장
            return recur(index + 1, output)  # 다음 박스로 재귀 호출

        return recur(0, [])
