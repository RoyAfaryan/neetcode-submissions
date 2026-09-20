class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = 0
        size = len(nums)

        while i < size:

            if nums[i] == val:
                nums.pop(i)
                size -= 1
                continue
            i+=1

        return len(nums)