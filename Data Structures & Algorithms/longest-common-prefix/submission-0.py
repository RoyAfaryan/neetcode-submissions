class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # base case
        if len(strs) == 1:
            return strs[0]

        strs.sort()
        print(strs)
        prefix = strs[0]
       
        i = 0

        while i < len(strs) or prefix is None:
            if strs[i].startswith(prefix):
                i+=1
                continue
            else:
                prefix = prefix[0:len(prefix)-1]
                i = 0
            
        return prefix


        