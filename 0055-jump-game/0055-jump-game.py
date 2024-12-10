class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0  # 현재 위치에서 도달 가능한 최대 인덱스
        for i, jump in enumerate(nums):
            if i > max_reachable:  # 현재 위치를 도달할 수 없으면 False
                return False
            max_reachable = max(max_reachable, i + jump)  # 도달 가능한 최대 범위 갱신
            if max_reachable >= len(nums) - 1:  # 마지막 인덱스에 도달 가능하면 True
                return True
        return False


        