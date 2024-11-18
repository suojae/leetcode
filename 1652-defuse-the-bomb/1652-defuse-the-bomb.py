class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        
        if k == 0:
            return [0] * n
        
        answer_array = []
        for i in range(n):
            if k > 0:
                answer_array.append(sum(code[(i + j) % n] for j in range(1, k + 1)))
            elif k < 0:
                answer_array.append(sum(code[(i + j) % n] for j in range(k, 0)))

        return answer_array
