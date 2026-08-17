class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
          
        triplets = []
        size = len(nums)
        left, mid, right = 0, 1, size - 1
        
        nums.sort()
        print(nums)

        while left < right - 1:
            
            while mid < right:
                if nums[mid] + nums[right] == -nums[left]:
                    if [nums[left], nums[mid], nums[right]] not in triplets:
                        triplets.append([nums[left], nums[mid], nums[right]]) 
                    mid += 1
                elif nums[mid] + nums[right] < -nums[left]:
                    mid += 1
                else:
                    right -= 1

            left += 1
            mid = left + 1
            right = size - 1

        return triplets
