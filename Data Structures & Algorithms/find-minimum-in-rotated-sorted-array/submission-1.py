class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) - 1
        smallest = nums[0]

        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] < smallest:
                smallest = nums[mid]

            left_diff = abs(nums[mid] - nums[left])
            right_diff = abs(nums[mid] - nums[right])

            if left_diff < right_diff:
                left = mid + 1
            else:
                right = mid - 1

        return smallest
