from collections import defaultdict

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
      
        items.sort()

        prices = []
        max_beauties = []
        max_beauty = 0

        for price, beauty in items:
            if beauty > max_beauty:
                max_beauty = beauty
            prices.append(price)
            max_beauties.append(max_beauty)
        
        answer_array=[]

        def binary_search(prices, target):
            left, right = 0, len(prices)-1
            result=-1

            while left<=right:
                mid=(left+right)//2
                if prices[mid] <= target:
                    result = mid
                    left = mid+1
                else:
                    right = mid-1
            
            return result  

        for query in queries:
            index = binary_search(prices, query)
            if index >= 0:
                answer_array.append(max_beauties[index])
            else:
                answer_array.append(0)
        return answer_array
