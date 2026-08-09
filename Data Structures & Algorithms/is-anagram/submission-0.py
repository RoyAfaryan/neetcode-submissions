class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Logic
        # 1. Create two hashmaps
        # 2. Store each char with frequency
        # 3. Compare

        n = len(s)
        m = len(t)

        d1 = {}
        d2 = {}

        for i in range(n):
            if s[i] in d1:
                d1[s[i]] += 1
            else:
                d1[s[i]] = 1

        for i in range(m):
            if t[i] in d2:
                d2[t[i]] += 1
            else:
                d2[t[i]] = 1    

        return d1 == d2