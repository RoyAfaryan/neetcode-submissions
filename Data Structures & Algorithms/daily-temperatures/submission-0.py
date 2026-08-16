class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        size = len(temperatures)
        res = [0] * size
        stack = []

        for i in range(size-1):
            stack.append((temperatures[i], i))
            if temperatures[i] < temperatures[i+1]:
                while stack:
                    if stack[-1][0] < temperatures[i+1]:
                        res[stack[-1][1]] = i+1 - stack[-1][1]
                        stack.pop()
                    else:
                        break
                
        
        return res