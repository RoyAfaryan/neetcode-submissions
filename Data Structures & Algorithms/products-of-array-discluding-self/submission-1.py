import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Logic
        # MOST EFFICIENT OPTIMAL SOLUTION
        # 1. Set prefix equal to 0,
        # 2. Set suffix prefix + 2
        # 3. Calculate first element
        # 4. Calculate 0:prefix, prefix+2:end
        # 5. Calculate final element

        total = math.prod(nums)
        size = len(nums)
        res = [0]*size

        for i in range(size):
            
            if nums[i] != 0:
                res[i] = int(total / nums[i])
            else:
                res[i] = math.prod(nums[0:i]) * math.prod(nums[i+1:size])

        return res