class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        # create copy
        ans = [x for x in nums]

        # add concatenation
        for num in nums:
            ans.append(num)

        return ans
