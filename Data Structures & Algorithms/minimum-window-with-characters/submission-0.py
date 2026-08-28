class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        t_map = {char: t.count(char) for char in set(t)}
        s_map = defaultdict(int)

        left, right = 0, 0
        size = len(s)
        ss = ""
        minSS = " " * (size + 1)
        have, need = 0, len(t_map)

        while right < size:
            s_map[s[right]] += 1

            if s[right] in t_map:
                if s_map[s[right]] == t_map[s[right]]:
                    have += 1

            if have == need:
                while have == need:
                    ss = s[left:right+1]
                    if len(ss) < len(minSS):
                        minSS = ss
                    
                    s_map[s[left]] -= 1
                    if s[left] in t_map and s_map[s[left]] < t_map[s[left]]:
                        have -= 1
                    
                    if s_map[s[left]] == 0:
                        del s_map[s[left]]

                    left+=1

            right+=1

           
        return "" if len(minSS) > size else minSS
