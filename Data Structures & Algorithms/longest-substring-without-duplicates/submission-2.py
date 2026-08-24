class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        # Logic:
        # 1. 

        hashset = set()
        ss = ""
        size = len(s)
        maxSS = ""
        l, r = 0, 0

        while r < size:
            if s[r] not in hashset:
                hashset.add(s[r])
            else:
                while s[r] in hashset:
                    hashset.discard(s[l])
                    l+=1
                continue
                
            r+=1   
            ss = s[l:r]


            if len(maxSS) < len(ss):
                maxSS = ss


        return len(maxSS)
