class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1
        smallest = nums[0]
        offset = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] < smallest:
                smallest = nums[mid]
                offset = mid

            left_diff = abs(nums[mid] - nums[left])
            right_diff = abs(nums[mid] - nums[right])

            if left_diff < right_diff:
                left = mid + 1
            else:
                right = mid - 1

        copy = nums[offset:len(nums)] + nums[0:offset]

        start, end = 0, len(copy) - 1
        print(copy)
        while start <= end:
            mid = start + (end - start) // 2
            if copy[mid] == target:
                return (mid + offset) % len(copy)
            elif copy[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
        
        return -1
