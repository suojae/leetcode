class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
    
        def max_box_value(max_val: int) -> int:
            stores_needed = 0
            for quantity in quantities:
                stores_needed += (quantity + max_val - 1) // max_val
            return stores_needed
        
        left = 1
        right = max(quantities)
        answer = right

        while left <= right:
            mid = (left + right) // 2
            
            if max_box_value(mid) <= n:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer
