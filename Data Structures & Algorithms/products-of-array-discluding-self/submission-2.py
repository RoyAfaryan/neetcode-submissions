import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    

        total = math.prod(nums)
        size = len(nums)
        res = [0]*size

        for i in range(size):
            
            if nums[i] != 0:
                res[i] = int(total / nums[i])
            else:
                res[i] = math.prod(nums[0:i]) * math.prod(nums[i+1:size])

        return res