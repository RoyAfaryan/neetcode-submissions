class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Logic:
        # 1. Create a dictionary
        # 2. Add every value in nums to dict with the count
        # 3. Sort the dictionary by values
        # 4. Return 0-k elements


        res = defaultdict(int)

        for num in nums:
            res[num] += 1

        return [key for key, value in sorted(res.items(), key=lambda item: item[1], reverse = True)[0:k]] 

       