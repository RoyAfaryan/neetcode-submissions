class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Logic:
        # 1. put s1 into hashmap with frequency
        # 2. create sliding window with the size of s1
        # 3. store each value in hashmap, compare s1 and s2
        # 4. 
        
        if len(s1) > len(s2):
            return False

        left, right = 0, len(s1)

        s1Map = {item: s1.count(item) for item in set(s1)}
        s2Map = {item: s2[left:right].count(item) for item in set(s2[left:right])}
    

        while right < len(s2):
            print(s1Map)
            print(s2Map)
            if s1Map == s2Map:
                return True
            else:
                if s2Map.get(s2[right]) is not None:
                    s2Map[s2[right]] += 1
                else:
                    s2Map[s2[right]] = 1

                s2Map[s2[left]] -= 1

                if s2Map[s2[left]] == 0:
                    del s2Map[s2[left]]
                left+=1
                right+=1

            
        return s1Map == s2Map