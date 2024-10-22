from collections import deque
import heapq

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        dQ = deque([root])  
        answer_heap = []
        
        while dQ:
            sum = 0
            for _ in range(len(dQ)):  
                node = dQ.popleft()
                sum += node.val
                if node.left:
                    dQ.append(node.left)
                if node.right:
                    dQ.append(node.right)
            
            heapq.heappush(answer_heap, -sum)  # 최대 힙
            
        if len(answer_heap) < k:
            return -1
        
        for _ in range(k - 1):
            heapq.heappop(answer_heap)
            
        return -heapq.heappop(answer_heap)  
