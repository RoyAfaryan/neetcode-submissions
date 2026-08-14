class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Logic:
        # 1. Convert to set for O(1) lookup
        # 2. Find the starting element of each sequence: nums[i] != nums[i] - 1
        # 3. Do lookups for each start of the sequence in increments

        s = set(nums)
        size = len(nums)
        longest_sequence = 0
        starters = []
        
        for i in range(size):
            if nums[i] - 1 not in s:
                starters.append(nums[i])
        print(starters)
        temp = 0
        i = 0
        k = 0
        while i < len(starters):
            if starters[i] + k in s:
                temp+=1
                k+=1
                continue
            else:
                if temp > longest_sequence:
                    longest_sequence = temp
                temp = 0
                k = 0
            i+=1
            

        return longest_sequence
