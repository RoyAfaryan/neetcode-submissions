class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        hashtable = defaultdict(int)

        for num in nums:
            hashtable[num]+=1
            if hashtable[num] > 1:
                return num

                