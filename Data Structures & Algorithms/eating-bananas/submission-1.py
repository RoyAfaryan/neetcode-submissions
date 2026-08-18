class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # O(nlogm) solution

        n = len(piles)
        m = max(piles)
        
        start, end = 1, m
        res = m

        # binary search
        while start <= end:
            mid = start + (end-start) // 2
            temp = 0

            # calculate
            for i in range(n):
                temp += math.ceil(piles[i]/mid)
            
            # check viability
            if temp <= h:
                if mid < res:
                    res = mid
                end = mid - 1
                
            elif temp > h:
                start = mid + 1
            
        return res