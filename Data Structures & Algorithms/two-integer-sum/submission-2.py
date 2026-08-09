class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Logic:
        # hashmap approach
        # 1. store everything into a hashmap with key being nums[i] and val being index
        # 2. iterate through list 
        # 3. 

        size = len(nums)
        d = {}

        for i in range(size):
            d[nums[i]] = i

        for i in range(size):
            temp = target - nums[i]
            if temp in d and i is not d[temp]:
                return [i, d[temp]]

        