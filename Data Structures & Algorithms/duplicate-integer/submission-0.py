class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # Logic:
        # 1. Initialize empty hashmap
        # 2. Iterate through loop and put value + count (key, val)
        # 3. If any count > 1; return True, else false


        d = {}
        size = len(nums)

        for i in range(size):
            if nums[i] in d:
                return True
            else:
                d[nums[i]] = 1

        return False